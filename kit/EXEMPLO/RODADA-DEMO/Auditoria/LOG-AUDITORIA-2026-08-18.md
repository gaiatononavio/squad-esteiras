# LOG DE AUDITORIA · RODADA-DEMO · 2026-08-18
> Auditor Apartado (subagente de contexto novo, somente leitura). Nenhum artefato da rodada foi editado.
> Escopo: integridade e fidelidade da deliberação — não mérito de domínio.

## 1. O que foi lido
- **Na íntegra (alavancagem máxima):** `02-dossie-EH-A.md` e `04-blueprint-EH-A.md`.
- **Na íntegra (verificação cruzada independente):** os 4 pareceres (`Pareceres/PARECER-P1..P4-EH-A.md`), `03-diagnostico-priorizado.md`, `06-registro-de-decisoes.md`, `05-catalogo-building-blocks.md`, `00-lote.md`, `01-triagem.md`. Os artefatos são curtos; nada foi aceito só por resumo — todos os cruzamentos abaixo foram feitos contra o texto real em disco (Verdade do Disco cumprida).
- **Não lido:** cartas de papel em `kit/PERSONAS/` (não necessárias para os cruzamentos desta rodada; nenhum achado dependeu delas).

## 2. Checagem A — Conformidade (fatos verificados no disco)
- **4 elementos do dossiê:** presentes — pareceres (§2), conflitos expostos e não suprimidos (§3, três conflitos nomeados com os lados identificados), riscos (§4), recomendação (§5). ✔
- **Rótulo FICTÍCIA:** presente no cabeçalho dos 5 artefatos auditados e também em lote, triagem e nos 4 pareceres. Nenhuma deriva para descrição de instituição real. ✔
- **[ASSUNÇÃO]:** os números sensíveis estão todos marcados — ~900/dia, 20–30% de exceção, 90%/2% de critérios de parada (blueprint §6 marca "[ASSUNÇÃO, a calibrar no passo 1]"), 5% de amostragem (blueprint §4.4). Não encontrei assunção vestida de fato. Blueprint §8 declara "não medido" em vez de inventar número. ✔
- **DECs:** DEC-001..003, sequenciais, sem fantasma. Cascatas conferidas no destino: DEC-001→triagem (seleção consta), DEC-002→diagnóstico/blueprint/catálogo (consta), DEC-003→catálogo (consta). Divergências nominais registradas em DEC-002 batem com os pareceres reais. ✔ (ressalva de proveniência da DEC-001 no §4 abaixo)
- **5 critérios do diagnóstico:** os mesmos 5, na mesma ordem, da triagem ao diagnóstico; a única mudança de nota (variância de EH-A) é declarada e atribuída ao veto 2 do P4 em nota de rodapé — não houve troca de critério silenciosa. ✔
- **Blueprint separa decisão do papel × autoridade humana:** §7 explícito, com as perguntas do comitê/jurídico/segurança formuladas. ✔
- **Parecer P2 (Governança e Risco):** existe, veredito COM CONDIÇÕES, 6 condições. Conferi uma a uma contra o blueprint §4: as 6 estão lá, íntegras e marcadas "não removíveis" (dono nomeado; duas trilhas; segregação; métrica de guarda+amostragem+rollback; humano confirmando até comitê; minimização/retenção). ✔ Nenhuma condição foi contornada — a recomendação as embute em vez de escapar delas.

## 3. Checagem B — Red-team (o que cacei ativamente)
- **Consenso suspeito:** não encontrado. Os conflitos P1×P3 (BB-001 não existe como componente testado) e triagem×P4 (variância) estão expostos no dossiê §3 e no registro DEC-002, com o lado perdedor preservado.
- **Ganho × distribuição de casos:** enfrentado de frente (dossiê conflito 3; P4 checklist 4): tempo médio × headcount-hora, fila difícil que não encolhe. O clássico foi evitado. ✔
- **Aspiracional disfarçado de executável:** não — a recomendação é medir a fila real antes até do piloto sombra, e o blueprint se declara "especificação, NÃO sistema aprovado nem em construção".
- **Over-claim:** não — o registro de decisões mantém as três entradas como "pendente — recomendação do squad", explicando que sem ratificação humana nada vira decisão.
- **Número inflado:** não encontrado; custos "não medidos" declarados como tal.

## 4. Achados (os que importam)
1. **[REFINO] Fidelidade P4→blueprint incompleta em 2 exigências do piloto.** O parecer P4 §4 exige (item 3) *canal para o analista devolver "o modelo errou aqui" e isso virar métrica*, e (item 5) conversa registrada com ≥2 analistas *também sobre o que muda na rotina deles*. O blueprint §§5–6 herdou a taxonomia de exceção, a amostragem, o motivo na tela e a métrica por cliente — mas **não** o canal de devolução do analista como métrica, e reduziu a conversa do item 5 só à taxonomia. Como toda a recomendação da rodada se apoia no P4, essas duas ausências são exatamente o tipo de condição que evapora entre parecer e blueprint.
2. **[REFINO menor] Proveniência da DEC-001 ambígua.** `00-lote.md` (intake) já declara "Deliberação profunda: EH-A" — a seleção veio nomeada de fora. A DEC-001 registra a seleção como decisão do orquestrador na triagem, citando os 5 critérios. Ou o intake pré-decidiu (e a DEC deveria atribuir a seleção ao intake, com a triagem só confirmando), ou o campo "quem opinou" está impreciso. Não altera o desfecho; altera quem responde pela escolha — e proveniência é o negócio deste registro.
3. **[NOTA, sem ação obrigatória] Inconsistência interna do P3 harmonizada em silêncio.** O P3 §1 diz "loop de agente em um único ponto"; a espinha do próprio P3 (§4) e o §3 descrevem 2 loops. Dossiê e blueprint adotaram "2 pontos" — leitura correta da espinha, mas a harmonização não foi anotada. Registro aqui para a trilha.

## 5. Mérito de domínio — sinalizado e roteado (não julgado por mim)
- Se pilotar EH-A antes de EH-B é a prioridade certa, e se a forma workflow+2 loops é o melhor desenho: raia dos papéis do squad + autoridade-fonte humana (o diagnóstico já encaminha isso corretamente).
- Base legal LGPD, retenção de imagem, extração fora do ambiente: já roteados pelo próprio material às filas de jurídico/compliance/segurança — correto.

## 6. Veredito
**VALIDADO-COM-REFINOS.** Refinos: incorporar ao blueprint as 2 exigências do P4 hoje ausentes (achado 1) e corrigir por nota append-only a proveniência da DEC-001 (achado 2). Nenhum retrabalho estrutural; a deliberação está rigorosa, os conflitos estão expostos, as condições do P2 estão íntegras e o registro não over-claima.

*Auditor Apartado — recomendação sujeita a ratificação da autoridade-fonte humana; este log não é decisão.*
