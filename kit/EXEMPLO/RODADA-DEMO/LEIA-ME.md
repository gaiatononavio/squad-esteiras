# RODADA-DEMO — uma rodada completa, rodada de verdade

> **O que é isto.** Uma rodada inteira da skill `squad-esteiras`, executada de ponta a ponta em
> 2026-08-18 — não um exemplo redigido para *parecer* que rodou. Cada parecer foi emitido por um
> subagente de contexto novo carregando só a carta de papel e o lote; o dossiê, o diagnóstico, o
> blueprint e o catálogo foram compostos pelo orquestrador a partir dos pareceres; e a auditoria
> rodou **apartada** (subagente limpo, charter verbatim, recebendo só os artefatos + ponteiros —
> nunca o raciocínio de quem produziu). O auditor devolveu **validado-com-refinos** com dois
> achados reais de fidelidade, aplicados como notas/edições marcadas nos artefatos. O log dele
> está em `Auditoria/`.

> ⚠️ **As três esteiras do lote são FICTÍCIAS**, criadas para a demonstração. Nenhuma descreve
> processo real de nenhuma instituição; volumes e sistemas são inventados e marcados [ASSUNÇÃO].

## Ordem de leitura
1. `00-lote.md` — o intake: 3 esteiras fictícias, o que se sabe e o que se assume.
2. `01-triagem.md` — a triagem barata pelos 5 critérios; seleção de EH-A para o rito completo.
3. `Pareceres/` — os 4 pareceres (P1 arquitetura, P2 governança/risco, P3 produto/MCP, P4 dono da esteira), cada um emitido por subagente independente no formato da própria carta.
4. `02-dossie-EH-A.md` — o dossiê: pareceres, **3 conflitos expostos**, riscos, recomendação.
5. `03-diagnostico-priorizado.md` — o lote ranqueado pelos 5 critérios (artefato-fim 1).
6. `04-blueprint-EH-A.md` — a especificação de workflow + conector MCP + skill, pronta para engenharia avaliar (artefato-fim 2).
7. `05-catalogo-building-blocks.md` — o catálogo inaugurado, BB-001…BB-004 (artefato-fim 3).
8. `06-registro-de-decisoes.md` — DEC-001…003, append-only, todas como "recomendação pendente de ratificação humana" (comportamento correto: demonstração não tem autoridade real para ratificar).
9. `07-ficha-precedente-P-001.md` — a **destilação** da rodada (v1.1): a investigação de EH-A vira precedente reaproveitável, com a seção "o que NÃO transfere" e os gatilhos de aderência que uma rodada futura precisa responder antes de reusar. Inaugura o banco de precedentes (T6).
10. `Auditoria/LOG-AUDITORIA-2026-08-18.md` — o que o auditor leu, verificou e achou. *(Nota: a auditoria rodou sobre os artefatos 00–06; a ficha 07 foi destilada depois, na incorporação da memória entre rodadas — v1.1 — e será auditada na próxima rodada que a consumir.)*

## Mapa evento → mecanismo (o que cada momento da rodada demonstra)

| Evento observável nesta rodada | Onde ver | Mecanismo que ele demonstra |
|---|---|---|
| O P4 vetou a premissa "variância moderada e conhecida" da própria triagem, e a recomendação final mudou para "medir antes de pilotar" | `PARECER-P4` §3 · dossiê §3.2 | **Independência funcional dos pareceres** — o subagente não herdou o juízo do orquestrador; divergiu dele, sem coreografia |
| O P1 rebaixou a recomendação por qualidade de dado não demonstrada, contra o entusiasmo do desenho do P3 | `PARECER-P1` §3 · dossiê §3.1 | **Conflito exposto, não suprimido** — a divergência é o conteúdo do dossiê, não ruído a editar |
| O auditor achou duas exigências do P4 que haviam evaporado a caminho do blueprint, e uma proveniência errada na DEC | `Auditoria/LOG` · notas append-only no blueprint §§5–6.1 e no registro | **O firewall funcionando** — avaliação apartada pegando o produtor no ato, dentro da própria entrega; refino aplicado por quem produz, nunca pelo auditor (Princípio Zero) |
| As três DECs permanecem "recomendação pendente de ratificação" | `06-registro-de-decisoes.md` | **Ratificação é do humano** — sem autoridade real no loop, nada vira decisão; o mecanismo se recusa a fingir |
| Todo número não fornecido está marcado [ASSUNÇÃO]; toda esteira, rotulada FICTÍCIA | qualquer artefato | **Travas de honestidade** — assunção nunca vestida de fato |
| A investigação de EH-A virou a ficha P-001, com "o que não transfere" e gatilhos de aderência | `07-ficha-precedente-P-001.md` | **Destilação/memória entre rodadas** — a rodada seguinte parte do que esta aprendeu, sob teste de aderência |

## Escopo do exemplo (leia antes de generalizar)
Esta rodada mostra **um caminho** — EH-A atravessando o rito completo, com EH-B/EH-C só em triagem. Não exercita: consulta a precedentes na triagem (o banco nasceu vazio aqui), bloqueio do P2 (o veredito foi "com condições"), devolução para instrução, escotilha para o modo robusto, nem rodadas sucessivas consumindo o catálogo. É evidência de que o rito opera — não um tour pela ferramenta inteira.

## O que esta rodada demonstra (e o que não)
Demonstra: o rito completo operando — pareceres independentes, conflito não suprimido, auditoria fora do fluxo pegando o que o produtor não viu, registro com proveniência.
Não demonstra: que isso acelera uma esteira real — nenhum caso real foi tocado, nenhuma métrica de produção foi medida. É a operação do aparato de deliberação, com honestidade sobre onde ele para.

---
**Nota de versão (append-only, 18-08-2026):** esta rodada foi executada sob a v1.0/v1.1 da skill — os pareceristas receberam a triagem com os escores preliminares, prática que a v1.3 **proibiu** (cegamento, ratificado pela autoridade-fonte após parecer da sessão-mãe). O fato de o P4 ter vetado uma premissa da própria triagem mesmo tendo-a lido é evidência de independência funcional — mas não prova que a âncora nunca morde, e foi exatamente por isso que o cegamento virou regra. Rodadas futuras seguem a FASE 3 da v1.3.

**Nota de versão 2 (append-only, 18-08-2026):** a v1.4 ampliou a mesa para 6 cartas (P5 Segurança Adversarial e P6 Dados/Avaliação, convocadas por gatilho objetivo). Esta rodada rodou com a mesa de 4 — e, pelo critério da v1.4, EH-A teria convocado as duas (há LLM lendo documento de cliente → P5; há limiar de confiança no desenho → P6). Os ângulos não ficaram descobertos por acaso: apareceram espremidos nos pareceres de P1 (extração confiante e errada; confiança não calibrada) e P2 (três caixas via checklist) — foi exatamente essa compressão que motivou as cartas dedicadas. Uma rodada futura sobre caso análogo exercita a mesa completa.

**Nota de versão 3 (append-only, 2026-08-24):** a rodada futura anunciada acima existe: `../RODADA-2/` — executada sob as regras completas (cegamento auditável, mesa de 6 por gatilho, consumo do precedente P-001 com teste de aderência desafiado, governança do catálogo) e com desfecho diferente (devolução para instrução). E o blueprint desta rodada virou código: `/prototipo` (bancada, 8/8 testes).
