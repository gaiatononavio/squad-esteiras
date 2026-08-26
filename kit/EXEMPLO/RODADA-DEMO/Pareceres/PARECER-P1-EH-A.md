# PARECER P1 · EH-A — Validação de comprovante de residência (FICTÍCIA)

**Rodada:** RODADA-DEMO · 2026-08-18 · **Papel:** P1 — Arquiteto(a) de Dados e Engenharia

---

## 1. Pergunta-assinatura — "Isso roda com os sistemas e dados que existem — ou só no slide?"

Roda em grande parte com o que existe: o insumo já chega digitalizado por upload e o candidato a building block (extração de campos de documento não estruturado) cobre o núcleo técnico da tarefa. O ponto que o intake **não** demonstra é o acesso estruturado ao cadastro para o cotejo nome/endereço — sem confirmar como esse dado é consultado (API, base, tela), a etapa de "bate com o cadastro" ainda é slide. Com essa confirmação, a esteira é tecnicamente executável hoje em modo piloto.

## 2. Checklist

1. **Dado consumido e acessibilidade.** (a) Imagem/PDF do comprovante enviado pelo cliente — não estruturado, **exige extração** (OCR + extração de campos: nome, endereço, data, emissor); (b) registro cadastral do cliente (nome, endereço) para cotejo — **[ASSUNÇÃO]** existe em base estruturada e consultável em tempo de análise; o intake não informa via de acesso (API/consulta direta/tela legada) e essa é a lacuna de informação nº 1; (c) tabela de tipos de documento aceitos e janela de validade — **[ASSUNÇÃO]** hoje é regra tácita do analista, precisa ser explicitada como parâmetro.
2. **Natureza da tarefa: híbrida, com maioria determinística.** São regra pura: tipo de documento ∈ lista aceita; data dentro da janela; match exato de nome. Pedem julgamento (agente ou humano): legibilidade do documento, variações de grafia de nome/endereço (abreviações, nome social, endereço com complemento divergente) e suspeita de documento adulterado — esta última **não** deve ser resolvida por agente sem trilha, e o aspecto fraude/risco é raia de P2, sinalizo e roteio. Arquitetura indicada: workflow determinístico com loop de agente (ou fila humana) nos pontos de julgamento.
3. **Building block do catálogo.** A extração de campos (nome, endereço, data, emissor) resolve o coração do problema — transformar documento não estruturado em dado comparável. Fica de fora: o motor de regras de validação (tipo/janela), o cotejo com o cadastro (integração), o fluxo de devolução ao cliente (pedir reenvio) e a fila de exceção. Nota: o intake declara que **não existe catálogo formal** — este bloco é candidato inaugural, ou seja, **[ASSUNÇÃO]** ele ainda não está empacotado/testado como componente reutilizável; contar com ele como pronto seria otimismo.
4. **Modo de falha mais provável.** Extração confiante porém errada em documento de baixa qualidade (foto tremida, layout de emissor não visto no treino/regras): o campo sai preenchido, o cotejo "passa" ou "reprova" com base em dado errado. É **parcialmente detectável** automaticamente — score de confiança da extração + validações cruzadas (CEP×cidade, formato de data, emissor conhecido) capturam boa parte; o resíduo (nome plausível mas de outra pessoa, comprovante de terceiro) **só humano percebe**. Mitigação: threshold de confiança que roteia para humano, e amostragem contínua dos aprovados automáticos.
5. **Custo por caso (ordem de grandeza).** Inferência: centavos de real por documento (1–2 chamadas de extração + eventual chamada de julgamento em ~10–30% dos casos **[ASSUNÇÃO]** sobre a taxa de exceção); a ~900 casos/dia **[ASSUNÇÃO do lote]**, dezenas de reais/dia — irrelevante frente ao custo do analista. Integração: o custo dominante do projeto é a conexão com o cadastro e com o fluxo de reenvio ao cliente, não a IA. Manutenção: baixa-média — novos layouts de emissores e mudanças na lista de documentos aceitos exigem revisão periódica das regras/prompts.

## 3. Classificação de viabilidade

**Viável com integração nova** — a integração a nomear é a **consulta estruturada ao cadastro do cliente** (e, secundariamente, o gancho no fluxo de comunicação de reenvio). A extração em si é viável com o que existe. Exercendo meu poder de rebaixamento: como a qualidade do dado (variedade real de emissores/layouts e taxa de legibilidade) não está demonstrada, recomendo **pilotar com amostra** — rodar a extração em paralelo ao analista sobre um corte real de casos e medir concordância antes de qualquer automação de decisão. (A eventual remoção de revisão humana passa por comitê, conforme restrição do intake — decisão fora da minha raia.)

## 4. O que mais me preocupa

Que o "building block reaproveitável" ainda não exista como componente testado — a viabilidade inteira está apoiada num bloco que esta rodada apenas inaugura, e ninguém mediu sua acurácia sobre os documentos reais desta esteira.

---
*Todas as marcações **[ASSUNÇÃO]** indicam dado não fornecido pelo lote. Esteira fictícia, para demonstração.*
