# Protótipo de bancada · do blueprint ao código

> **O que é isto.** O blueprint da esteira EH-A (`kit/EXEMPLO/RODADA-DEMO/04-blueprint-EH-A.md`)
> saiu da rodada como "especificação pronta para engenharia avaliar". Esta pasta é a prova de que
> a especificação é executável: os dois building blocks que ela criou, materializados em código
> que roda, com testes verdes. É o trecho **prototipação → produtização** do ciclo, depois do
> trecho **diagnóstico → deliberação** que o resto do repositório demonstra.

> ⚠️ **BANCADA, não produto.** Dados 100% sintéticos (cadastro fictício, comprovantes fictícios
> com aviso no cabeçalho de cada arquivo). Nada aqui foi aprovado, toca dado real ou dispensa
> qualquer condição de governança do blueprint — a fase 1 (humano confirma todo veredito) está
> **codificada**, não prometida. E uma honestidade técnica: a extração da bancada é determinística
> sobre documentos sintéticos; em produção ela seria o loop de agente do blueprint (modelo lendo
> documento real). O que a bancada isola e prova é o **contrato** (entrada → saída → erro) e o
> workflow de governança em volta — a extração por modelo é substituível atrás do mesmo contrato.

## O que tem aqui

| Arquivo | O que é | Bloco do catálogo |
|---|---|---|
| `extrator.py` | Extração de campos + score de confiança (heurístico, não calibrado) + match tolerante de nome | BB-001 (núcleo) |
| `doc_extract_server.py` | BB-001 exposto como **servidor MCP** (tool `doc_extract`, transporte stdio) — a forma produtizável que o blueprint escolheu | BB-001 (conector) |
| `valida_comprovante.py` | O workflow do blueprint: regras determinísticas + julgamento restrito + rotas de exceção + trilha por caso | BB-002 (workflow) |
| `skill-valida-comprovante/SKILL.md` | Os critérios de aceite empacotados no formato de Agent Skill — o bloco de conhecimento versionado | BB-002 (skill) |
| `dados_sinteticos/` | Cadastro fictício (3 clientes) + 6 comprovantes fictícios, um por ramo do contrato | — |
| `testes/test_bancada.py` | 8 testes cobrindo caminho feliz, nome abreviado, data vencida, tipo limítrofe, documento corrompido, titularidade de terceiro, cadastro indisponível e trilha obrigatória | — |

## Rodar

```bash
cd prototipo
python3 testes/test_bancada.py        # sem dependências; deve terminar em "8/8 testes passando"
pip install mcp && python3 doc_extract_server.py   # opcional: sobe o conector MCP em stdio
```

Saída da última execução registrada (2026-08-24): **8/8 testes passando**.

## O que os testes provam (e o que não)

Provam que as exigências dos pareceres viraram comportamento, não prosa: caso limítrofe **vai a humano com motivo em vez de reprovação automática** (veto do P4), confiança abaixo do piso **roteia em vez de decidir** (P1/P6), extração falhada **devolve tipado em vez de falhar silencioso** (contrato §2), e **toda resposta carrega a trilha por caso** (condição de governança do P2). Não provam: acurácia de extração sobre documento real (não medida — é o que o piloto sombra do blueprint mede), volume, latência, nem qualquer métrica de produção.

## Efeito no catálogo

Com esta bancada, BB-001 e BB-002 mudam de status no catálogo: de **especificado** para **existente-em-bancada** — reaproveitáveis por qualquer rodada futura que precise de extração documental ou de validação com match tolerante (a Rodada 2, sobre a esteira EH-B, consome exatamente isso).
