# P-001 · Validação documental com cotejo contra cadastro · rodada RODADA-DEMO · 2026-08-18
> Origem: dossiê `02-dossie-EH-A.md` · blueprint `04-blueprint-EH-A.md` · DECs 001–003
> Rótulo da esteira de origem: **FICTÍCIA (demonstração)** · Status da recomendação de origem: **recomendação pendente de ratificação**
> Ficha destilada na FASE 7 da rodada de demonstração — inaugura o banco de precedentes (T6).

## 1. O problema-tipo, decomposto em elementos
Cliente envia documento não estruturado; analista confere caso a caso contra regras enumeráveis + um cotejo com registro interno, e decide aprovar/reprovar/pedir reenvio.
- Tipo de dado: documento não estruturado (imagem/PDF) + dado pessoal cadastral não sensível.
- Tipo de ato final: aprovação/reprovação de item cadastral — **reversível**, sem consequência externa imediata (mas com efeito latente até detecção).
- Tipo de julgamento: híbrido — regras determinísticas (tipo aceito, janela de data, match exato) + julgamento restrito (legibilidade, variação de grafia).
- Integrações tocadas: consulta estruturada ao cadastro (a lacuna nº 1 de viabilidade); fluxo de devolução ao cliente.

## 2. A forma de solução investigada
Workflow determinístico com loop de agente em 2 pontos (extração; match tolerante), consumindo conector `doc-extract` (BB-001, acesso) e skill `valida-comprovante` (BB-002, conhecimento). Descartados: só conector (não resolve orquestração), agente ponta a ponta (caro e menos auditável quando 3 de 4 checagens são regra).

## 3. Recomendação de origem e o porquê
**Pilotar em modo sombra, precedido de instrução da fila real** — não automatizar direto. Variável dominante: a fração automatizável real nunca foi medida, e todo o ganho depende dela.

## 4. Exceções-tipo e achados operacionais
Legibilidade/formato; **titularidade de terceiro** (regra tácita do analista, nunca escrita); tipo/data limítrofe. Fração [ASSUNÇÃO] ~20–30%. Achados que o desenho ingênuo não previa: o "não sei" precisa cair em fila humana com o motivo na tela (nunca loop de reenvio); métrica por cliente (3+ reenvios), não por caso; canal de devolução do analista virando métrica.

## 5. Condições de governança recorrentes
Prováveis em qualquer caso parecido: dono humano nomeado; duas trilhas (deliberação + execução); segregação extração ≠ decisão ≠ auditoria; métrica de guarda + amostragem de aprovados + rollback; minimização/retenção da imagem. Específica deste caso: fila de comitê para qualquer remoção de revisão humana (restrição declarada no intake fictício).

## 6. O QUE NÃO TRANSFERE
- A **reversibilidade alta** do ato: é o que baixou o custo do erro aqui. Caso parecido com ato pouco reversível (ex.: encerramento, concessão) muda a recomendação inteira — ver a linha EH-C do diagnóstico.
- O volume (~900/dia) e a fração de exceção (20–30%): **[ASSUNÇÃO] nunca medidos** — não herdar como se fossem dados.
- A taxonomia de exceção: é da esteira, vive na cabeça de quem a opera; cada caso novo exige a própria conversa com ≥2 analistas.
- A clareza regulatória assumida: documento de comprovação cadastral é terreno simples; documento com implicação legal (procuração, ordem judicial) não herda nada daqui.

## 7. Gatilhos de aderência (responder antes de aplicar este precedente)
1. O ato final é igualmente reversível, e o custo latente até detecção é comparável?
2. A parte determinística cobre ≥ metade das checagens, com julgamento restrito a leitura/matching?
3. O documento de entrada é do mesmo gênero (comprovação cadastral) ou carrega implicação legal?
4. A taxonomia de exceção foi medida com a operação — ou está sendo assumida de novo?
5. O `doc-extract` (BB-001) já existe como componente testado no momento da consulta, ou segue especificado?
