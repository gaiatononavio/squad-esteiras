# -*- coding: utf-8 -*-
"""Testes da bancada · blueprint EH-A executável em nível de contrato.

Rodar da pasta `prototipo/`:  python3 -m pytest testes/ -v   (ou: python3 testes/test_bancada.py)

Cada caso sintético cobre um ramo do contrato do blueprint (§2) e das
exigências dos pareceres P4 (limítrofe vai a humano com motivo, nunca
reprovação automática) e P1/P6 (piso de confiança roteia, não decide).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from valida_comprovante import (  # noqa: E402
    APROVAR, HUMANO, REENVIAR, carregar_cadastro, validar,
)

BASE = os.path.join(os.path.dirname(__file__), "..", "dados_sinteticos")
CADASTRO = carregar_cadastro(os.path.join(BASE, "cadastro.json"))


def _caso(arquivo: str, cliente: str):
    with open(os.path.join(BASE, "comprovantes", arquivo), encoding="utf-8") as f:
        return validar(arquivo, f.read(), cliente, CADASTRO)


def test_caminho_feliz_aprova_com_humano_confirmando():
    v = _caso("c1_luz_ok.txt", "CLI-001")
    assert v.veredito == APROVAR
    assert v.motivo == "CHECAGENS_OK_FASE1_HUMANO_CONFIRMA"
    assert v.confianca >= 0.75
    assert any("humano confirma" in t for t in v.trilha)  # fase 1 sempre


def test_nome_abreviado_passa_no_match_tolerante():
    v = _caso("c2_agua_nome_abreviado.txt", "CLI-001")  # "Maria A. Souza Ficticia"
    assert v.veredito == APROVAR
    assert any("match tolerante ok" in t for t in v.trilha)


def test_data_fora_da_janela_recomenda_reenvio():
    v = _caso("c3_telefone_data_vencida.txt", "CLI-002")
    assert v.veredito == REENVIAR
    assert v.motivo == "DATA_FORA_JANELA"


def test_tipo_nao_aceito_vai_a_humano_nao_reprova_automatico():
    v = _caso("c4_gas_tipo_nao_aceito.txt", "CLI-003")  # exigência do P4
    assert v.veredito == HUMANO
    assert v.motivo == "TIPO_NAO_ACEITO_AVALIAR"


def test_documento_corrompido_cai_no_piso_de_confianca():
    v = _caso("c5_corrompido.txt", "CLI-001")
    assert v.veredito == HUMANO
    assert v.motivo in {"CONFIANCA_ABAIXO_DO_PISO", "NENHUM_CAMPO_EXTRAIDO", "DOCUMENTO_ILEGIVEL"}
    assert v.confianca < 0.75


def test_titularidade_de_terceiro_vai_a_humano_com_motivo():
    v = _caso("c6_terceiro_titular.txt", "CLI-003")  # locador ≠ titular do cadastro
    assert v.veredito == HUMANO
    assert v.motivo == "TITULARIDADE_A_CONFIRMAR"


def test_cadastro_indisponivel_devolve_nunca_decide():
    v = _caso("c1_luz_ok.txt", "CLI-999")
    assert v.veredito == HUMANO
    assert v.motivo == "CADASTRO_INDISPONIVEL"


def test_trilha_por_caso_sempre_presente():
    for arq, cli in [("c1_luz_ok.txt", "CLI-001"), ("c5_corrompido.txt", "CLI-001")]:
        v = _caso(arq, cli)
        assert len(v.trilha) >= 2  # condição de governança: trilha reconstituível


if __name__ == "__main__":
    falhas = 0
    for nome, fn in sorted({k: v for k, v in globals().items() if k.startswith("test_")}.items()):
        try:
            fn()
            print(f"PASS  {nome}")
        except AssertionError as e:
            falhas += 1
            print(f"FAIL  {nome}: {e}")
    print(f"\n{8 - falhas}/8 testes passando")
    sys.exit(1 if falhas else 0)
