# DIAGNÓSTICO PRIORIZADO · RODADA-DEMO · 2026-08-18
> Rótulo do lote: **FICTÍCIO — criado para demonstração** (as 3 esteiras).
> Critérios (sempre estes 5, nesta ordem): 1 custo do erro · 2 reversibilidade · 3 volume × variância · 4 building block reaproveitável · 5 clareza regulatória
> Escala qualitativa; nenhuma nota numérica foi calibrada.

| # | Esteira | Rótulo | C1 custo do erro | C2 reversib. | C3 volume×variância | C4 building block | C5 clareza reg. | Recomendação | Por quê (1 frase) |
|---|---------|--------|------------------|--------------|---------------------|-------------------|-----------------|--------------|-------------------|
| 1 | EH-A · comprovante de residência | fictícia | baixo–médio | alta | alto / [ASSUNÇÃO]* | cria BB-001/BB-002 | clara [ASSUNÇÃO] | **pilotar (modo sombra), após instrução da fila real** | Erro barato e reversível + o bloco que cria (`doc-extract`) paga a si mesmo fora da esteira. |
| 2 | EH-B · divergência cadastral | fictícia | médio | média (exige trilha) | médio / moderada | consome BB-001; cria BB-003 | clara [ASSUNÇÃO] | **rodada própria depois de EH-A** | Herda de graça o `doc-extract`; deliberar antes do bloco existir seria especificar no ar. |
| 3 | EH-C · encerramento com pendências | fictícia | alto | baixa no pior caso | baixo / alta | parcial: cria BB-004 | cinzenta (implicação legal) | **não automatizar a decisão agora; especificar BB-004 como apoio ao humano** | Custo do erro alto + variância alta + área cinzenta: automatizar a consulta, nunca a decisão. |

\* A triagem havia classificado a variância de EH-A como "moderada e conhecida"; o **veto 2 do P4** derrubou a premissa — a taxonomia de exceção nunca foi escrita. Fica [ASSUNÇÃO] até medição.

## Leitura do ranking
EH-A é a #1 não porque seja a mais valiosa em si, mas porque combina o erro mais barato do lote com o efeito de portfólio mais alto: o conector `doc-extract` que ela obriga a construir é consumível de imediato por EH-B e por qualquer esteira que leia documento de cliente — o critério 4 puxa a fila inteira, não um item. A recomendação, porém, é **pilotar, não automatizar**: os quatro pareceres convergiram em que a fração automatizável real é a variável dominante e ninguém a mediu (ver conflito 3 do dossiê).

EH-C ilustra o outro lado do mesmo critério: ali o que se automatiza com segurança não é a decisão (custo do erro alto, reversibilidade baixa, terreno cinzento), e sim a **consulta consolidada de pendências** (BB-004) — building block que encurta o trabalho do humano sem tirar o humano do ato. Priorizar esteira não é binário automatiza/não-automatiza; é escolher qual pedaço de cada esteira merece virar bloco.

O que derrubaria esta leitura: se a medição da fila real de EH-A mostrar fração de exceção muito acima dos [ASSUNÇÃO] 20–30% do P4, o ganho encolhe e EH-B (variância genuinamente menor) pode assumir a ponta. A divergência interna está exposta na seção 3 do dossiê — este diagnóstico adota a posição do P4 (medir antes de pilotar) por ser a mais barata de estar errada.

## O que este diagnóstico NÃO é
Não é aprovação: é instrução completa para a decisão humana. A prioridade aqui não dispensa a fila de autoridade externa listada no dossiê (comitê, jurídico/compliance) — nenhum piloto começa sem ela.
