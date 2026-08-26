# T4 — CATÁLOGO DE BUILDING BLOCKS (vivo; atualizado a cada rodada)

```markdown
# CATÁLOGO DE BUILDING BLOCKS · atualizado em {data} · rodada {RODADA}
> Building block = capacidade já resolvida e reaproveitável entre esteiras.
> Status possíveis: existente (onde vive) · especificado (blueprint) · candidato (só nomeado).

| ID | Building block | Tipo | O que faz | Status | Origem | Reaproveitável por | Observações |
|----|----------------|------|-----------|--------|--------|--------------------|-------------|
| BB-001 | … | acesso (tool MCP) | … | existente | esteira {X} | esteiras que precisem de {operação} | … |
| BB-002 | … | conhecimento (skill) | … | especificado | blueprint {Y} | … | … |
| BB-003 | … | material (template/resource) | … | candidato | parecer P3 da rodada {Z} | … | ainda não especificado |

> **Tipo** segue a taxonomia de blocos: **acesso** (tool/conector MCP — capacidade executável com credencial),
> **conhecimento** (skill/procedimento), **material** (template, contexto endereçável), **distribuição** (plugin
> que empacota os anteriores). Blocos de conhecimento no nível de investigação vivem no banco de precedentes (T6).

## Regras do catálogo
1. **ID sequencial, nunca reaproveitado.** Bloco aposentado permanece, marcado como aposentado.
2. Um bloco só vira "existente" com ponteiro para onde ele vive de verdade — nunca de memória.
3. A cada rodada, o parecer P3 alimenta este catálogo: o que a esteira consome e o que cria.
4. Reúso registrado aqui é insumo direto do critério 4 do diagnóstico (T2).
5. **A métrica que este catálogo serve:** automatizar N esteiras é trabalho; fazer a esteira N+1
   custar menos que a N porque as anteriores viraram bloco é plataforma. Se o catálogo cresce e
   nenhuma rodada consome bloco de rodada anterior, ele é inventário, não plataforma — e isso é
   um achado a reportar, não a esconder.

## Governança do catálogo (ratificada 18-08-2026 — contra a deriva da rodada 10)
6. **Append-only:** definição não se reescreve; correção é nota nova datada; bloco superado
   permanece, marcado e apontando para o sucessor.
7. **Definição canônica única por bloco:** um bloco = uma definição. Se uma rodada precisar de algo
   "quase igual mas diferente", ou é o mesmo bloco (emenda por nota, via DEC) ou é bloco novo com a
   diferença nomeada — nunca uma segunda definição implícita do mesmo bloco.
8. **Consultar antes de definir:** nenhum bloco novo entra sem busca prévia por equivalente no
   catálogo, com o resultado declarado ("não há equivalente" também se escreve).
9. **Passe de deduplicação:** periodicamente (sugestão: a cada ~3 rodadas, junto com a auditoria
   periódica do cânone), procurar blocos duplicados e definições tardias que contradigam antigas;
   conflito achado vira nota + DEC, nunca edição silenciosa.
```
