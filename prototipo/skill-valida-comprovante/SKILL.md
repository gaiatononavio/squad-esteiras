---
name: valida-comprovante
description: "BB-002 · PROTÓTIPO DE BANCADA (dados sintéticos). Critérios de aceite de comprovante de residência empacotados como skill: tipos aceitos, janela de validade, piso de confiança, match tolerante de nome e rotas de exceção. Use quando um agente precisar validar um comprovante FICTÍCIO de bancada contra um cadastro sintético, consumindo a tool doc_extract do conector MCP doc-extract-bancada. NÃO usar com documento ou dado real: isto é a demonstração executável do blueprint EH-A, não um sistema aprovado."
---

# valida-comprovante (BB-002, bancada)

Procedimento de decisão do blueprint EH-A, empacotado no formato de skill para mostrar a **forma produtizável** do bloco de conhecimento: os critérios saem da cabeça do analista e viram procedimento versionado que qualquer agente consumidor executa igual.

## Critérios (os mesmos de `valida_comprovante.py` — uma fonte, duas embalagens)
1. Extraia os campos com a tool `doc_extract`. Extração falhada (ok=false) → **devolver a humano com o motivo**; nunca decida sobre extração falhada.
2. Confiança abaixo de **0.75** → devolver a humano (`CONFIANCA_ABAIXO_DO_PISO`). Confiança é sinal de roteamento, não medida.
3. Tipo de serviço fora de {luz, agua, telefone} → devolver a humano (`TIPO_NAO_ACEITO_AVALIAR`) — caso limítrofe **nunca** é reprovação automática.
4. Emissão há mais de **90 dias** da data de referência → recomendar reenvio (`DATA_FORA_JANELA`). Data futura → humano (anomalia).
5. Nome do titular × cadastro pelo **match tolerante** (abreviação/acento/inicial). Não bateu → devolver a humano (`TITULARIDADE_A_CONFIRMAR`), com os dois nomes na tela.
6. Tudo ok → `APROVAR_RECOMENDADO`. **Fase 1 sempre: humano confirma.** Nenhuma decisão autônoma nesta bancada.
7. Toda resposta carrega a **trilha por caso** (checagens executadas, na ordem). Resposta sem trilha é resposta inválida.

## O que esta skill não decide
Autonomia parcial (fase 2), retenção da imagem, base legal e amostragem de produção são as condições de governança do blueprint (§4 e §7) — fila de autoridade humana. Esta skill implementa o procedimento; não dispensa nenhuma aprovação.
