# RODADA-2 — a segunda rodada, executada sob as regras completas (v1.4)

> **O que é isto.** A segunda rodada real da skill, executada em 2026-08-24 sobre a esteira EH-B (FICTÍCIA, herdada do lote da RODADA-DEMO). Diferente da primeira, esta rodou com **tudo** que a skill ganhou depois: cegamento dos pareceristas, mesa de 6 com convocação por gatilho, consumo de precedente com teste de aderência, blocos existentes-em-bancada, e governança do catálogo. E teve desfecho **diferente** da R1: devolução para instrução — o terceiro estado que a R1 não exercitava.

> ⚠️ Esteira e dados **FICTÍCIOS**; assunções marcadas [ASSUNÇÃO]; recomendações pendentes de ratificação (demonstração).

## Ordem de leitura
1. `00-contexto.md` — o caso (o que os pareceristas receberam).
2. `01-triagem-orquestrador.md` — escores, decomposição, convocação com gatilhos. **Os pareceristas não viram este arquivo** (cegamento).
3. `02-insumo-pareceristas.md` — memória disponível + o teste de aderência do precedente P-001, entregue aos pareceristas com o dever de desafiá-lo.
4. `03-instrucao-de-spawn.md` — a instrução verbatim de spawn, registrada para o cegamento ser auditável.
5. `Pareceres/` — os **6** pareceres (mesa fixa + P5 Segurança e P6 Avaliação, convocadas por gatilho).
6. `04-dossie-EH-B.md` — dossiê com conflitos expostos e a recomendação de devolução.
7. `05-registro-de-decisoes.md` — DEC-R2-001…003 (numeração com namespace, continuando o registro único).
8. `06-ficha-precedente-P-002.md` — a destilação: o precedente do problema-tipo "conciliação com escrita".
9. `Auditoria/` — o log do auditor apartado desta rodada.

## Mapa evento → mecanismo (o que esta rodada demonstra que a R1 não demonstrava)

| Evento observável | Onde ver | Mecanismo |
|---|---|---|
| Os pareceristas não leram a triagem; a instrução de spawn está registrada e proíbe | `03-instrucao-de-spawn.md` · cabeçalhos dos pareceres | **Cegamento** (v1.3) — quem opina recebe o caso, nunca o juízo do orquestrador; e o cegamento é auditável, não declarado |
| P5 e P6 sentaram à mesa por gatilho registrado (credencial de escrita; score/limiar) | `01-triagem-orquestrador.md` §Convocação | **Convocação por gatilho, não por organograma** (v1.4) |
| O teste de aderência do P-001 foi adotado em parte e **corrigido em dois pontos** pelos pareceristas | dossiê §3.3 · pareceres P1/P4/P6 | **Precedente é hipótese a desafiar** — o reúso acelera a instrução sem herdar erro (trava anti-ancoragem funcionando) |
| A investigação partiu do que a R1 aprendeu: condições recorrentes herdadas, extração descartada com porquê, match consumido da bancada | `02-insumo-pareceristas.md` · pareceres | **Efeito plataforma** — a esteira N+1 partiu de investigação pronta, e o que não transferia foi rejeitado por escrito |
| P5 descreveu o ataque mais barato (divergência induzida + prevalência por recência = sequestro de endereço) e o controle fora do modelo que o quebra | `PARECER-P5` §5 | **Segurança adversarial como carta, não como checklist** — "instrução não é imposição" aplicado a um ataque concreto |
| P6 rebaixou: score heurístico de bancada não carrega decisão de escrita; "contrato provado ≠ número provado" | `PARECER-P6` §3 | **Poder de rebaixar por falta de calibração** (P6) |
| A recomendação final foi **devolver para instrução** com perguntas específicas — não aprovar, não matar | dossiê §5 · DEC-R2-002 | **O terceiro estado** — o rito sabe dizer "ainda não dá para decidir isto", que é o que separa deliberação de carimbo |
| A sobreposição BB-003 × match da bancada foi resolvida em UMA definição canônica, via DEC com cascata aplicada no catálogo da R1 | DEC-R2-003 · nota no catálogo da R1 | **Governança do catálogo** (v1.3) — consultar antes de definir; dedup por decisão, não por edição silenciosa |
| Duas divergências nominais preservadas no registro (P5×padrão de modelo no match; P2×P5 na segunda caixa) | DEC-R2-002 | **Divergência nominal** — consenso apagado não ensina nada |

## Escopo
Esta rodada não produziu blueprint — de propósito: a recomendação foi devolver para instrução, e blueprint antes da regra de prevalência existir seria aspiracional disfarçado de executável. O caminho "recomendação → blueprint → protótipo" está demonstrado na R1 + `/prototipo`. Segue não exercitado: bloqueio (P2/P5 ficaram em "com condições"), escotilha para o modo robusto, e cartas convocáveis (UX/resiliência/fornecedores — gatilhos ausentes, registrado).

---
**Nota pós-auditoria (append-only, 2026-08-24):** a auditoria apartada desta rodada devolveu **validado-com-refinos** com um achado real de fidelidade — os blocos criados pelo P3 não tinham entrado no catálogo como candidatos (T4 regra 3); corrigido por nota append-only no catálogo da R1 (BB-005…BB-008). Observação menor registrada para rodadas futuras: o insumo aos pareceristas deve comunicar o FATO da convocação sem antecipar expectativa de desenho (evitar "no desenho provável" — borda do cegamento). Log em `Auditoria/`.
