# T5 — REGISTRO DE DECISÕES (contínuo da organização; append-only)

> O registro é UM só e **atravessa rodadas** — a numeração nunca recomeça. É o par do banco de
> precedentes: o banco guarda o que se aprendeu; o registro, quem decidiu o quê e quando.

```markdown
# REGISTRO DE DECISÕES · {ORGANIZAÇÃO/SQUAD}
> Append-only: nada se apaga. Correção é nota nova; decisão superada permanece, marcada
> como superada. Numeração com **namespace de rodada: DEC-R{n}-{nnn}** (ex.: DEC-R1-001,
> DEC-R2-001) — a rodada no identificador garante unicidade global e mata a referência
> ambígua (o primo brando do DEC-fantasma). Número real e sequencial dentro da rodada —
> NUNCA invente nem cite DEC que não existe aqui. Registro único, contínuo entre rodadas.

## DEC-R{n}-001 · {título} · {data}
- **O quê:** …
- **Por quê:** …
- **Quem opinou:** P1 / P2 / P3 / P4 (ponteiros aos pareceres)
- **Divergência nominal:** {papel} divergiu porque … (consenso apagado não ensina nada;
  se não houve divergência, escreva "sem divergência registrada" — não invente uma)
- **Ratificação:** {autoridade humana}, em {data} — sem ratificação humana, a entrada
  fica como "recomendação do squad", nunca como decisão
- **Cascata:** artefatos a atualizar → verificação feita NO DESTINO (nunca declarada de memória)

## DEC-R{n}-002 · …
```

> Este registro é a trilha da **deliberação**. Não é log de execução caso a caso — são duas
> trilhas distintas, e um produto em operação precisa das duas.
