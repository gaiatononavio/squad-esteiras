# -*- coding: utf-8 -*-
"""BB-002 `valida-comprovante` · workflow do blueprint EH-A · PROTÓTIPO DE BANCADA.

Implementa a espinha do blueprint (04-blueprint-EH-A.md), fase 1 SEMPRE:
o veredito é RECOMENDAÇÃO; um humano confirma. Nenhuma decisão autônoma.

Contrato (blueprint §2):
  entrada : texto do comprovante + id do cliente (cadastro sintético)
  saída   : veredito proposto {APROVAR_RECOMENDADO | REENVIAR_RECOMENDADO | DEVOLVER_HUMANO}
            + motivo codificado + campos extraídos + confiança + trilha por caso
  erro    : ilegível / tipo não reconhecido / cadastro indisponível / confiança
            abaixo do piso → o caso é DEVOLVIDO à fila humana COM o motivo na tela
            (nunca decidido, nunca falha silenciosa, nunca loop de reenvio automático).

Condições de governança do blueprint refletidas aqui (não removíveis):
  - segregação: extração (extrator.py) ≠ decisão (este módulo) ≠ auditoria (fora);
  - trilha por caso: todo retorno carrega a lista de checagens executadas;
  - piso de confiança roteia a humano; tipo/titularidade limítrofes vão a humano
    com motivo, não a reprovação automática (exigência do parecer P4).

⚠️ BANCADA: dados 100% sintéticos; datas comparadas contra uma DATA_REFERENCIA
fixa para os testes serem determinísticos. Isto NÃO é sistema aprovado nem em
construção — é o blueprint provado executável no nível de contrato.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import date

from extrator import extrair, match_nome_tolerante

TIPOS_ACEITOS = {"luz", "agua", "telefone"}
JANELA_DIAS = 90
PISO_CONFIANCA = 0.75
DATA_REFERENCIA = date(2026, 8, 1)  # fixa, para bancada determinística

APROVAR = "APROVAR_RECOMENDADO"
REENVIAR = "REENVIAR_RECOMENDADO"
HUMANO = "DEVOLVER_HUMANO"


@dataclass
class Veredito:
    caso_id: str
    veredito: str
    motivo: str
    confianca: float
    campos: dict = field(default_factory=dict)
    trilha: list = field(default_factory=list)

    def as_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)


def carregar_cadastro(caminho: str) -> dict:
    with open(caminho, encoding="utf-8") as f:
        return {c["id"]: c for c in json.load(f)}


def validar(caso_id: str, texto_documento: str, cliente_id: str, cadastro: dict | None) -> Veredito:
    trilha: list = [f"caso={caso_id} cliente={cliente_id} data_ref={DATA_REFERENCIA.isoformat()}"]

    # 0 · cadastro disponível? (erro do contrato: devolve, não decide)
    if not cadastro or cliente_id not in cadastro:
        trilha.append("cadastro indisponivel ou cliente inexistente")
        return Veredito(caso_id, HUMANO, "CADASTRO_INDISPONIVEL", 0.0, {}, trilha)
    ref = cadastro[cliente_id]

    # 1 · extração (BB-001; em produção, loop de agente #1)
    ext = extrair(texto_documento)
    trilha += [f"[extracao] {t}" for t in ext.trilha]
    if not ext.ok:
        return Veredito(caso_id, HUMANO, ext.motivo_erro or "EXTRACAO_FALHOU", ext.confianca, ext.campos, trilha)

    # 2 · piso de confiança roteia a humano (nunca decide no escuro)
    if ext.confianca < PISO_CONFIANCA:
        trilha.append(f"confianca {ext.confianca} < piso {PISO_CONFIANCA}")
        return Veredito(caso_id, HUMANO, "CONFIANCA_ABAIXO_DO_PISO", ext.confianca, ext.campos, trilha)

    # 3 · regra determinística: tipo de emissor
    if ext.tipo_servico not in TIPOS_ACEITOS:
        trilha.append(f"tipo '{ext.tipo_servico}' fora da lista aceita {sorted(TIPOS_ACEITOS)} — limítrofe vai a humano (P4)")
        return Veredito(caso_id, HUMANO, "TIPO_NAO_ACEITO_AVALIAR", ext.confianca, ext.campos, trilha)
    trilha.append(f"tipo '{ext.tipo_servico}' aceito")

    # 4 · regra determinística: janela de validade
    try:
        emissao = date.fromisoformat(ext.campos.get("data_emissao", ""))
    except ValueError:
        trilha.append("data de emissao ausente/invalida")
        return Veredito(caso_id, HUMANO, "DATA_ILEGIVEL", ext.confianca, ext.campos, trilha)
    idade = (DATA_REFERENCIA - emissao).days
    if idade < 0:
        trilha.append(f"data futura ({emissao}) — anomalia vai a humano")
        return Veredito(caso_id, HUMANO, "DATA_FUTURA_ANOMALIA", ext.confianca, ext.campos, trilha)
    if idade > JANELA_DIAS:
        trilha.append(f"documento com {idade} dias > janela de {JANELA_DIAS}")
        return Veredito(caso_id, REENVIAR, "DATA_FORA_JANELA", ext.confianca, ext.campos, trilha)
    trilha.append(f"data dentro da janela ({idade} dias)")

    # 5 · julgamento restrito: match tolerante de nome (loop #2 do blueprint)
    ok_nome, detalhe = match_nome_tolerante(ext.campos.get("nome", ""), ref["nome"])
    trilha.append(f"[match nome] {detalhe}")
    if not ok_nome:
        trilha.append("titularidade nao confirmada — vai a humano com motivo (P4), nunca reprovacao automatica")
        return Veredito(caso_id, HUMANO, "TITULARIDADE_A_CONFIRMAR", ext.confianca, ext.campos, trilha)

    # 6 · veredito proposto — FASE 1: humano confirma (condição do blueprint)
    trilha.append("todas as checagens ok — recomendacao de aprovacao (fase 1: humano confirma)")
    return Veredito(caso_id, APROVAR, "CHECAGENS_OK_FASE1_HUMANO_CONFIRMA", ext.confianca, ext.campos, trilha)
