# T6 — FICHA DE PRECEDENTE (o banco de precedentes; contínuo, atravessa rodadas)

> Uma ficha por esteira deliberada a fundo, destilada no fim da rodada (FASE 7) — **inclusive quando a
> recomendação foi "não automatizar"** (precedente negativo poupa a mesma investigação duas vezes).
> ID sequencial contínuo (P-001, P-002…), nunca reaproveitado. Ficha superada permanece, marcada como superada.
> Precedente é **hipótese a desafiar**, nunca resposta pronta: quem o aplica escreve o teste de aderência.

```markdown
# P-{nnn} · {título do problema-tipo} · rodada {RODADA} · {data}
> Origem: dossiê {ponteiro} · blueprint {ponteiro, se houver} · DECs {números}
> Rótulo da esteira de origem: [FICTÍCIA | real documentada] · Status da recomendação de origem:
> [ratificada | recomendação pendente | superada por P-{nnn}]

## 1. O problema-tipo, decomposto em elementos
A esteira em uma frase, e os elementos que permitem casar casos futuros:
- Tipo de dado: … (documento não estruturado? cadastro? transacional? pessoal/sensível?)
- Tipo de ato final: … (aprovar/reprovar? corrigir registro? encerrar? reversível?)
- Tipo de julgamento: … (o que é regra determinística, o que exige interpretação)
- Integrações tocadas: …

## 2. A forma de solução investigada
Conector MCP / skill / workflow (loops de agente onde) — e por que as alternativas caíram.
Building blocks consumidos/criados (ponteiros ao catálogo T4).

## 3. Recomendação de origem e o porquê
Automatizar / pilotar / não automatizar — em 2–3 frases, com a variável dominante nomeada.

## 4. Exceções-tipo e achados operacionais
As exceções que o P4 levantou, a fração estimada [ASSUNÇÃO se for o caso], e o que a operação
ensinou que o desenho ingênuo não previa.

## 5. Condições de governança recorrentes
As condições do P2 que provavelmente se repetem em casos parecidos (dono nomeado, duas trilhas,
segregação, métrica de guarda + amostragem, minimização/retenção…), e as que foram específicas deste caso.

## 6. O QUE NÃO TRANSFERE (a coluna que dá honestidade ao reúso)
Explícito e obrigatório: o que desta investigação era específico desta esteira e NÃO deve ser
assumido num caso parecido (volume, taxonomia de exceção, terreno regulatório, integração…).
Ficha sem esta seção não entra no banco.

## 7. Gatilhos de aderência
As 3–5 perguntas que um caso futuro precisa responder para saber se este precedente se aplica.
(Ex.: "o ato é igualmente reversível?", "a taxonomia de exceção foi medida ou é assunção?")
```

## Como consultar (na FASE 2 de cada rodada)
1. Decomponha a esteira nova nos mesmos elementos da seção 1.
2. Compare com as fichas existentes; para cada match, escreva o **teste de aderência**: o que é igual, o que difere, **o que do precedente não transfere** (partindo da seção 6 da ficha).
3. Entregue matches + testes aos pareceristas como insumo. O precedente acelera a instrução; **não substitui parecer** — o P4 mantém o poder de derrubar a analogia, e analogia sem teste de aderência é achado de auditoria.
