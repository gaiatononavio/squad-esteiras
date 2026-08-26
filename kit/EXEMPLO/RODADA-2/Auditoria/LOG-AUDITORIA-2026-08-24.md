# LOG DE AUDITORIA · RODADA-2 · 2026-08-24 · Auditor Apartado (contexto novo)

> Princípio Zero respeitado: nenhum artefato da rodada foi editado. Este log é o único arquivo gravado.

## O que li na íntegra (verdade do disco, pelas ferramentas de arquivo)
- `04-dossie-EH-B.md`, `05-registro-de-decisoes.md`, `06-ficha-precedente-P-002.md`, `LEIA-ME.md` (os 4 auditados)
- Os **6 pareceres** em `Pareceres/` (P1–P6, na íntegra — necessários para cruzar dossiê × pareceres)
- `00-contexto.md`, `01-triagem-orquestrador.md`, `02-insumo-pareceristas.md`, `03-instrucao-de-spawn.md`
- `../RODADA-DEMO/07-ficha-precedente-P-001.md`, `../RODADA-DEMO/05-catalogo-building-blocks.md` (com as duas notas append-only de 24/08), `kit/TEMPLATES/T4_Catalogo_Building_Blocks.md`

## O que confiei por verificação pontual (grep), não por leitura integral
- `prototipo/README.md`: confirmadas verbatim as âncoras citadas pelos pareceres — "score de confiança (heurístico, não calibrado)", "8/8 testes passando", `match_nome_tolerante` (linhas 21, 32, 36).
- `../RODADA-DEMO/06-registro-de-decisoes.md`: confirmada a existência de DEC-001…003 e da nota de renumeração DEC-R1-001…003 (numeração de R2 é contínua, sem fantasma).

## Dupla checagem — A) Conformidade (tudo verificado no disco)
- **4 elementos do dossiê:** presentes (§2 pareceres, §3 conflitos expostos, §4 riscos, §5 recomendação). OK.
- **Rótulo FICTÍCIA:** presente no cabeçalho dos 4 auditados e dos 6 pareceres. OK.
- **[ASSUNÇÃO]:** volume ~250/dia, amostra/limiares do piloto (P3 §5), fração de exceção (P4) — todos marcados; nenhuma assunção vestida de fato encontrada.
- **DECs:** DEC-R2-001…003, sequenciais, namespace T5 v1.2, continuidade com R1 provada pela nota de renumeração. Nenhuma DEC fantasma citada (ficha P-002 cita R2-001…003; todas existem).
- **5 critérios:** a triagem usa C1–C5 declarados; sem troca de critério no meio.
- **Blueprint:** não existe — **de propósito** (devolução para instrução; LEIA-ME §Escopo justifica). A separação "papel decide × autoridade humana" está no dossiê §6 + filas externas de P2/P5/P6. Não é lacuna: blueprint aqui seria "aspiracional disfarçado de executável", exatamente o que o red-team caça.
- **P2 obrigatório:** existe, COM CONDIÇÕES C1–C6; as condições entraram na recomendação (dossiê §5) e na DEC-R2-002. OK.
- **Cegamento:** instrução de spawn registrada (`03`) proíbe verbatim a leitura de `01-triagem`; insumos listados não contêm escores; pareceres não citam escores da triagem. Auditável e respeitado. Observação menor registrada abaixo (achado 2).
- **Governança T4 (busca prévia):** P3 declara consulta ao catálogo e resolve a sobreposição BB-003 × `match_nome_tolerante` por definição canônica única. Citação "T4 regras 6–8" conferida contra o template: regras 6 (append-only), 7 (canônica única), 8 (consultar antes de definir) existem. Não é citação fantasma.
- **Convocação por gatilho:** P5 (credencial de escrita) e P6 (score/limiar) — gatilhos registrados na triagem, ambos emitiram parecer substantivo (não decorativo: P5 traz o ataque mais barato; P6 rebaixa). Convocáveis sem gatilho (UX/resiliência/fornecedores) não convocadas, com registro. OK.

## Dupla checagem — B) Red-team (caçado ativamente)
- **Consenso suspeito:** NÃO — duas divergências nominais preservadas (P5 × padrão EH-A sobre modelo no match; P2 "atenuado" × P5 "presente" na segunda caixa) e conferidas contra os pareceres originais: fiéis, não editadas para fechar redondo. O teste de aderência do orquestrador foi corrigido em 2 pontos pelos pareceristas e o dossiê registra a correção (anti-ancoragem funcionando).
- **Ganho sem enfrentar distribuição:** enfrentado (P4 §4: "derruba o tempo médio sem encolher a fila que dói"; dossiê risco 5).
- **Aspiracional disfarçado de executável:** evitado pela devolução; nenhum piloto prometido sem amostra.
- **Over-claim:** NÃO — registro, ficha e nota de cascata dizem "recomendação pendente de ratificação"; bancada consistentemente rebaixada a "contrato provado ≠ componente operacional ≠ número provado".
- **Contorno de bloqueio do P2:** NÃO — C1–C6 incorporadas; P2 e P5 declaram explicitamente a conversão em BLOQUEIO se o gate for por instrução.
- **Analogia forçada:** NÃO — teste de aderência por escrito, desafiado; reversibilidade alta de P-001 rejeitada por P2/P3; "o que não transfere" da P-002 escrito com honestidade (incl. "match de endereço segue sem código: não citar como existente").
- **Condição por texto vendida como controle:** NÃO — pareceres exigem credencial/permissão, e nomeiam o anti-padrão.
- **Rodada sem destilação:** NÃO — ficha P-002 criada + nota de cascata no catálogo.
- **Curto-e-vago:** NÃO encontrado; alternativas descartadas com porquê (P3 §1), contratos explícitos (P3 §3).

## Achados
1. **(Refino que importa) Catálogo não recebeu os blocos que a rodada CRIOU.** P3 "cria" `cadastro-read`, `cadastro-write` (condicionado), skill `resolve-divergencia` e o workflow `concilia-cadastro` (PARECER-P3 §2.2 e §3; ficha P-002 §2) — mas a única cascata no catálogo foi a promoção do BB-003 (DEC-R2-003). T4 regra 3 ("a cada rodada, o parecer P3 alimenta este catálogo: o que a esteira consome e o que cria") pede o registro ao menos como **candidato** (BB-005…), como se fez com BB-003/BB-004 na R1. Sem isso, a esteira N+2 que precise ler cadastro não encontra o candidato no índice de reúso — a informação vive só dentro da ficha P-002, e o critério C4 do diagnóstico fica cego a ela. Correção barata: nota append-only no catálogo, via quem produz (não eu — Princípio Zero).
2. **(Menor, registrar sem exigir)** O insumo aos pareceristas (`02`, §final) comunica os gatilhos de convocação com a frase "score/limiar **no desenho provável**" — um fragmento de expectativa de desenho do orquestrador vazando à mesa inteira. O cegamento de escores/juízos foi respeitado; isto é borda. Fica como observação para a mantenedora da skill: comunicar o fato da convocação sem prever o desenho.

## Fatos verificados de forma independente (amostra)
- P2 §5(b) diz "atenuado" e P5 §1 diz "SIM" na segunda caixa → dossiê §3.2 fiel.
- P5 tem exatamente 6 condições; P2 tem C1–C6 → dossiê §5 fiel ("C1–C6 do P2 e as 6 do P5").
- P6: "contrato provado ≠ número provado — os 8/8 testes provam rotas, não taxas" (§3) → dossiê §3.3 fiel.
- Proibição de "terceira versão" (P6 §5) → ficha P-002 §5 fiel.
- Vetos 1–3 do P4 → dossiê riscos 3 e 5 e recomendação (a)–(c) fiéis.
- "Recência sozinha nunca decide" (P5 cond. 6) → ficha §5 fiel.

## Veredito lavrado
**VALIDADO-COM-REFINOS.** Refino único de substância: achado 1 (catálogo). Mérito de domínio (se devolver era a decisão certa, se a forma P3 é a melhor) não julgado — fora da minha raia; roteado à autoridade-fonte.
