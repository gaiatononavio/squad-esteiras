# -*- coding: utf-8 -*-
"""BB-001 `doc-extract` · PROTÓTIPO DE BANCADA (dados 100% sintéticos).

Extrai nome, endereço, data de emissão e emissor de um comprovante de
residência FICTÍCIO em texto, devolvendo também um score de confiança.

Honestidade do protótipo (leia antes de julgar):
- Em produção, esta extração seria o "loop de agente #1" do blueprint EH-A
  (um modelo lendo documento real não estruturado). A bancada usa extração
  DETERMINÍSTICA sobre documentos sintéticos de texto porque o que ela isola
  e prova é o CONTRATO (entrada → saída → erro) e o workflow em volta —
  a extração por modelo é substituível atrás deste mesmo contrato.
- A "confiança" aqui é heurística declarada (fração de campos encontrados,
  degradada por linhas corrompidas). Confiança reportada NÃO é probabilidade
  calibrada de acerto — vale para roteamento, nunca como medida (parecer P1/P6).
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field, asdict

CAMPOS = ("emissor", "nome", "endereco", "data_emissao")

# Emissores fictícios reconhecidos pela bancada e o tipo de serviço de cada um.
EMISSORES_SINTETICOS = {
    "LUZBRAS DISTRIBUIDORA FICTICIA": "luz",
    "AGUAS EXEMPLO SANEAMENTO FICTICIO": "agua",
    "TELEFONICA DEMO FICTICIA": "telefone",
    "GASNORTE EXEMPLO FICTICIO": "gas",          # tipo fora da lista aceita → exceção
    "STREAMFLIX ENTRETENIMENTO FICTICIO": "outro",
}


def _norm(texto: str) -> str:
    t = unicodedata.normalize("NFD", texto)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", t).strip().upper()


@dataclass
class ResultadoExtracao:
    ok: bool
    campos: dict = field(default_factory=dict)
    tipo_servico: str | None = None
    confianca: float = 0.0
    motivo_erro: str | None = None      # preenchido quando ok=False
    trilha: list = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)


def extrair(texto_documento: str) -> ResultadoExtracao:
    """Contrato do BB-001: texto do comprovante → campos + confiança, ou erro tipado."""
    r = ResultadoExtracao(ok=False)
    if not texto_documento or len(texto_documento.strip()) < 20:
        r.motivo_erro = "DOCUMENTO_ILEGIVEL"
        r.trilha.append("documento vazio ou curto demais")
        return r

    linhas = [l.strip() for l in texto_documento.splitlines() if l.strip()]
    corrompidas = sum(1 for l in linhas if "�" in l or re.search(r"[#]{3,}", l))

    texto_norm = _norm(texto_documento)
    emissor = next((e for e in EMISSORES_SINTETICOS if e in texto_norm), None)
    if emissor:
        r.campos["emissor"] = emissor
        r.tipo_servico = EMISSORES_SINTETICOS[emissor]
        r.trilha.append(f"emissor reconhecido: {emissor} (tipo={r.tipo_servico})")
    else:
        r.trilha.append("emissor NAO reconhecido na base sintetica")

    m = re.search(r"TITULAR:\s*(.+)", texto_documento, re.IGNORECASE)
    if m:
        r.campos["nome"] = m.group(1).strip()
    m = re.search(r"ENDERECO:\s*(.+)", _norm_keep_lines(texto_documento), re.IGNORECASE)
    if m:
        r.campos["endereco"] = m.group(1).strip()
    m = re.search(r"EMISSAO:\s*(\d{4}-\d{2}-\d{2})", _norm_keep_lines(texto_documento))
    if m:
        r.campos["data_emissao"] = m.group(1)

    achados = len(r.campos)
    r.confianca = round((achados / len(CAMPOS)) * (0.6 if corrompidas else 1.0), 2)
    r.trilha.append(f"campos encontrados: {achados}/{len(CAMPOS)}; linhas corrompidas: {corrompidas}; confianca={r.confianca}")

    if achados == 0:
        r.motivo_erro = "NENHUM_CAMPO_EXTRAIDO"
        return r
    r.ok = True
    return r


def _norm_keep_lines(texto: str) -> str:
    t = unicodedata.normalize("NFD", texto)
    return "".join(c for c in t if unicodedata.category(c) != "Mn").upper()


def match_nome_tolerante(nome_doc: str, nome_cadastro: str) -> tuple[bool, str]:
    """Loop #2 do blueprint (julgamento restrito): match tolerante a abreviação/acento.

    Regra da bancada: sobrenome final igual + cada token do nome mais curto deve
    ser prefixo/inicial de um token correspondente do mais longo, em ordem.
    """
    a, b = _norm(nome_doc).split(), _norm(nome_cadastro).split()
    if not a or not b:
        return False, "nome ausente"
    if a[-1] != b[-1]:
        return False, f"sobrenome diverge ({a[-1]} x {b[-1]})"
    curto, longo = (a, b) if len(a) <= len(b) else (b, a)
    i = 0
    for tok in curto[:-1]:
        alvo = tok.rstrip(".")
        while i < len(longo) - 1:
            cand = longo[i]
            i += 1
            if cand == alvo or cand.startswith(alvo) or (len(alvo) == 1 and cand[0] == alvo):
                break
        else:
            return False, f"token '{tok}' sem correspondencia"
    return True, "match tolerante ok"
