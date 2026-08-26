# CATÁLOGO DE BUILDING BLOCKS · atualizado em 2026-08-18 · RODADA-DEMO
> Catálogo inaugurado nesta rodada (não havia catálogo formal — restrição do intake).
> Todo conteúdo deriva de esteiras **FICTÍCIAS** de demonstração.
> Status possíveis: existente (onde vive) · especificado (blueprint) · candidato (só nomeado).

| ID | Building block | O que faz | Status | Origem | Reaproveitável por | Observações |
|----|----------------|-----------|--------|--------|--------------------|-------------|
| BB-001 | `doc-extract` (conector MCP) | Extrai nome, endereço, data e emissor de documento não estruturado, com score de confiança | **especificado** | blueprint EH-A | EH-B e qualquer esteira que leia documento de cliente | Acurácia **não medida** — é a assunção de maior alavancagem da rodada (parecer P1) |
| BB-002 | `valida-comprovante` (skill) | Critérios de aceite de comprovante empacotados (tipos, janela, tolerância de match) | **especificado** | blueprint EH-A | Canais que recebem comprovante (app, atendimento) | Depende da taxonomia de exceção ainda não documentada (veto 2 do P4) |
| BB-003 | Comparação fuzzy de nome/endereço | Score de similaridade tolerante a abreviação/acento/complemento | candidato | triagem EH-B (+ loop #2 do blueprint EH-A) | EH-A (match de nome), EH-B (divergência cadastral) | Ainda não especificado; forte sobreposição com o loop de match de EH-A — unificar quando EH-B for deliberada |
| BB-004 | Consulta consolidada de pendências | Uma consulta que reúne o que hoje exige 4 telas (saldo, produtos, débitos, restrições) | candidato | triagem EH-C | EH-C e [ASSUNÇÃO] outras esteiras de relacionamento/encerramento | Bloco de **apoio ao humano** — o diagnóstico recomenda automatizar a consulta, nunca a decisão de EH-C |

## Regras do catálogo (herdadas do T4)
1. ID sequencial, nunca reaproveitado; bloco aposentado permanece marcado.
2. Um bloco só vira "existente" com ponteiro para onde vive de verdade — nunca de memória.
3. Cada rodada alimenta este catálogo via parecer P3 (consome/cria).
4. Reúso registrado aqui é insumo direto do critério 4 do diagnóstico.

---
**NOTA DE STATUS (append-only, 2026-08-24):** BB-001 `doc-extract` e BB-002 `valida-comprovante` ganharam **protótipo de bancada** em `/prototipo` (código real, 8/8 testes passando, dados 100% sintéticos): status passa de *especificado* para **existente-em-bancada**, com ponteiro real (`prototipo/doc_extract_server.py`, `prototipo/valida_comprovante.py`, `prototipo/skill-valida-comprovante/`). *Existente-em-produção* continua NÃO existindo — a bancada prova o contrato, não a operação. Definições originais intactas (append-only).

**NOTA DE PROMOÇÃO PROPOSTA (append-only, 2026-08-24, cascata da DEC-R2-003 — recomendação pendente de ratificação):** a RODADA-2 propôs resolver a sobreposição BB-003 × `match_nome_tolerante` com **definição canônica única**: BB-003 `compara-cadastro` passa a ser O bloco de comparação fuzzy (nome: existente-em-bancada, extraído do BB-001; endereço: a especificar, hoje sem código), e BB-001 vira consumidor de BB-003. Nunca duas implementações de match no catálogo (T4 regras 6–8). Definições originais intactas.

**NOTA DE CANDIDATOS DA RODADA-2 (append-only, 2026-08-24, por refino da auditoria da R2 — T4 regra 3):** a RODADA-2 criou quatro blocos que entram como **candidatos** (origem: parecer P3 da RODADA-2; detalhe na ficha `../RODADA-2/06-ficha-precedente-P-002.md` §2): **BB-005** conector `cadastro-read` (acesso: leitura dos dois sistemas + histórico; reaproveitável por qualquer cotejo cadastral, incl. a lacuna nº 1 do P-001) · **BB-006** conector `cadastro-write` (acesso: correção de registro com snapshot obrigatório; **condicionado às C1–C6 do P2 e às 6 condições do P5**) · **BB-007** skill `resolve-divergencia` (conhecimento: regra de prevalência — **só escrevível após instrução da fila real**) · **BB-008** workflow `concilia-cadastro` (distribuição/orquestração). Nenhum tem código; status: candidato.
