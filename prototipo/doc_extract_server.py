# -*- coding: utf-8 -*-
"""BB-001 `doc-extract` exposto como SERVIDOR MCP · PROTÓTIPO DE BANCADA.

Materializa a forma que o blueprint EH-A escolheu para o bloco de maior reúso:
uma capacidade interna exposta como conector MCP (tool invocável, contrato
tipado), consumível por qualquer esteira que leia documento de cliente.

Rodar (transporte stdio):
    pip install mcp
    python3 doc_extract_server.py
Ou plugar num cliente MCP (ex.: Claude Code) via configuração stdio apontando
para este arquivo. Log vai para stderr — nunca stdout (corrompe o JSON-RPC).

⚠️ BANCADA: extração determinística sobre documentos SINTÉTICOS (ver
extrator.py para a nota de honestidade completa). Em produção, a extração
seria por modelo — atrás deste MESMO contrato. A descrição da tool abaixo é
tratada como prompt (dirige a seleção do modelo consumidor): mudá-la é mudar
comportamento, e entraria em controle de mudança.
"""
import sys

from extrator import extrair

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # dependência declarada, erro claro em vez de silencioso
    print("Instale o SDK: pip install mcp", file=sys.stderr)
    raise

mcp = FastMCP("doc-extract-bancada")


@mcp.tool()
def doc_extract(texto_documento: str) -> dict:
    """Extrai campos de um comprovante de residência SINTÉTICO (bancada).

    Recebe o texto de um comprovante fictício e devolve: campos extraídos
    (emissor, nome, endereco, data_emissao), tipo de serviço, score de
    confiança (heurístico, NÃO calibrado — use para roteamento, não como
    medida) e a trilha de checagens. Em caso de documento ilegível ou sem
    campos, devolve ok=false com motivo tipado — o consumidor DEVE rotear
    o caso a um humano, nunca decidir sobre extração falhada.
    """
    return extrair(texto_documento).as_dict()


if __name__ == "__main__":
    print("doc-extract (bancada) rodando em stdio", file=sys.stderr)
    mcp.run(transport="stdio")
