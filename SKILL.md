---
name: squad-esteiras
description: "Squad Virtual de Aceleração de Esteiras — monta e roda um squad de especialistas virtuais de dados que investiga, por rodada, quais esteiras de um lote são boas candidatas a automação, e produz: diagnóstico priorizado com critério explícito, blueprint de skill/conector MCP pronto para engenharia avaliar, e dois artefatos CONTÍNUOS que fazem cada rodada custar menos que a anterior — o catálogo de building blocks (capacidades reaproveitáveis) e o banco de precedentes (investigações reaproveitáveis, com teste de aderência). O squad DELIBERA e ESPECIFICA; nunca executa sobre caso real. A avaliação de qualidade roda APARTADA do fluxo: um auditor independente que só lê, nunca escreve — não 'lá no meio' do workflow. Use quando o usuário quiser priorizar esteiras para automação, especificar uma skill ou conector MCP a partir de um processo manual, montar um squad virtual de dados, ou rodar uma rodada de deliberação sobre um lote de esteiras. Adaptação da skill 'criar-estudio-simples' (auditor como subagente, tudo em um projeto); a escotilha para firewall pleno ('criar-estudio-robusto', validador em projeto separado) está documentada no fim."
---

# Squad Virtual de Aceleração de Esteiras

Um squad de especialistas virtuais que faz, em horas, o estudo que hoje espera um especialista humano ter agenda: pegar um lote de esteiras, deliberar qual vale automatizar primeiro e por quê, e sair com uma especificação que um time de engenharia consegue avaliar. O humano continua decidindo — o squad chega à decisão com o dossiê pronto, o conflito exposto e a auditoria feita.

> **O que esta skill NÃO é.** O squad não é uma esteira e não executa nada em produção: nenhum agente daqui toca dado real de cliente, sistema transacional ou caso individual. O objeto-fim de cada rodada é papel de engenharia — diagnóstico, blueprint, catálogo — que segue para humanos com autoridade real (engenharia, risco, compliance) avaliarem. Parecer de agente não substitui parecer humano de compliance; ele chega antes, para a reunião humana começar com a pergunta certa.

---

## Por que a auditoria roda APARTADA (o desenho central)

Avaliadores embutidos "no meio" do workflow compartilham contexto com quem produz — e um avaliador que viu o raciocínio do produtor tende a continuá-lo, não a testá-lo. Não é seguro assumir que um modelo avaliando o próprio fluxo o reprovaria; e mesmo que reprovasse, não daria para distinguir avaliação independente de continuação do próprio raciocínio.

Aqui a avaliação é um **órgão, não uma etapa**:

- O auditor roda em **contexto novo** (subagente limpo), com um **charter fixo** (`references/auditor_apartado.md`) que não pode ser editado para facilitar aprovação.
- Ele recebe **só os artefatos prontos + ponteiros ao registro de decisões** — nunca a justificativa de quem produziu.
- **Princípio Zero: ele só lê.** Nunca escreve nos artefatos; devolve veredito + achados + um prompt copiável de correção, e grava apenas no log dele (`{RODADA}/Auditoria/`).
- Quem produziu **não se autoaprova**: os refinos do auditor são aplicados antes de qualquer artefato ser dado por pronto.

Nesta versão o firewall é **por disciplina** (mesma sessão, contexto separado). Para firewall **por topologia** (auditor em projeto separado, sessão isolada, idealmente outro modelo), ver a escotilha no fim.

---

## Vocabulário

- **Esteira** — processo relacionado a um negócio (seguro, crédito, cadastro, cobrança…): um fluxo operacional hoje avaliado/conduzido caso a caso e candidato a automação. Não é esteira de desenvolvimento/CI-CD — se um dia o objeto for esse, muda o que se delibera, não a arquitetura do squad.
- **Building block** — capacidade já resolvida por uma esteira automatizada e reaproveitável por outras (ex.: extração de campo de um tipo de documento). O catálogo de building blocks é um dos três artefatos-fim.
- **Produtizar** — expor uma capacidade interna como produto usável por outras áreas, via conector MCP, skill ou workflow.
- **Carta de papel** — o documento que define um especialista virtual: missão, pergunta-assinatura, competências, poderes, checklist. É o prompt permanente do agente — e vale igual se o papel um dia for humano.
- **Pergunta-assinatura** — a única pergunta que aquele papel faz em toda deliberação. Garante que a preocupação dele seja levantada por padrão, não por lembrança.
- **Dossiê** — o produto real de uma deliberação: pareceres, conflitos entre eles **expostos** (nunca suprimidos), riscos, recomendação.
- **Precedente** — uma investigação já feita: a ficha destilada de uma esteira deliberada em rodada anterior (problema-tipo, solução proposta, exceções, condições de governança, o que transfere e **o que não transfere**). Inclui precedentes negativos ("não automatizar porque X" também é trabalho reaproveitável). Precedente é **hipótese a desafiar**, nunca resposta pronta.
- **Bloco** — na prática, um de quatro tipos: **acesso** (tool/conector MCP), **conhecimento** (skill, procedimento, precedente), **material** (template, contexto endereçável), **distribuição** (o pacote que junta os anteriores). O catálogo guarda os de capacidade; o banco de precedentes, os de conhecimento.

---

## O squad (mesa fixa de 4 + 2 por gatilho + 1 órgão externo)

A unidade de desenho não é o cargo — é a **pergunta-assinatura discriminante**. Carta nova só existe quando traz uma pergunta que nenhuma outra faz e que muda recomendações. Cada carta convocada custa um parecer por esteira profunda: roster inchado não é robustez, é consenso fabricado que ninguém lê — e custo de inferência é a variável que mais facilmente destrói o business case.

**Mesa fixa (toda esteira profunda):**

| Papel | Pergunta-assinatura | Poder |
|---|---|---|
| **Arquiteto(a) de Dados e Engenharia** (`kit/PERSONAS/P1`) | "Isso roda com os sistemas e dados que existem — ou só no slide?" | Opina; classifica viabilidade |
| **Governança e Risco Operacional** (`kit/PERSONAS/P2`) — LGPD, regulação bancária, segregação de funções | "Quem responde pelo caso que passar errado — e o ato é reversível?" | **Parecer obrigatório; pode bloquear** |
| **Produto, MCP e Skills** (`kit/PERSONAS/P3`) | "Isso vira conector MCP, skill ou workflow — e que building block existente já resolve parte?" | Opina; propõe a forma do artefato |
| **Dono(a) da Esteira** (`kit/PERSONAS/P4`) — a voz de quem opera o processo hoje | "O que acontece com o caso que não se parece com nenhum que já vimos?" | Opina; veta irrealismo operacional |

**Convocadas por gatilho objetivo (obrigatórias quando o gatilho está presente; a triagem registra a convocação e o gatilho):**

| Papel | Gatilho de convocação | Pergunta-assinatura | Poder |
|---|---|---|---|
| **Segurança Adversarial** (`kit/PERSONAS/P5`) | agente/LLM no fluxo · conteúdo externo/documento de cliente lido por modelo · credencial de sistema em componente automatizado | "O que um adversário faz com isso — e o que o impede de verdade?" | **Parecer obrigatório quando convocada; pode bloquear** (três caixas sem perna cortada por controle técnico) |
| **Ciência de Dados e Avaliação** (`kit/PERSONAS/P6`) | modelo, score, limiar de decisão ou métrica que dispara ato | "Essa conclusão sobrevive ao dado — e como saberemos quando deixar de sobreviver?" | **Parecer obrigatório quando convocada; pode rebaixar** recomendação apoiada em número sem calibração |

**Fora do fluxo:**

| Papel | Pergunta | Poder |
|---|---|---|
| **Auditor apartado** (`references/auditor_apartado.md`) | "O dossiê sustenta o que afirma — e o que ele está escondendo?" | **Só lê; nunca escreve; não é membro do squad** |

**Cartas convocáveis ainda não escritas** (escrevem-se na primeira convocação real, entrando no cânone via DEC): UX/service design (gatilho: interface humana relevante no desenho — cockpit, fila de exceção); continuidade/resiliência (gatilho: irreversibilidade e volume altos — fallback e operação manual); gestão de fornecedores (gatilho: dependência de terceiro no blueprint). Convocar carta sem gatilho presente é achado de auditoria (parecer decorativo); deixar de convocar com gatilho presente também.

**O que NUNCA vira carta**, por desenho: (a) segunda linha de defesa real — jurídico, compliance, auditoria interna, validação formal de modelo, análise formal de fairness: o squad **prepara a conversa** com eles (fila de autoridade externa, perguntas prontas), nunca os simula; (b) papéis de execução — backend, RPA, MLOps, SRE, treinamento: o lugar deles é o **blueprint como handoff**, não a mesa de deliberação. Nenhuma recomendação de automação sai sem o parecer de Governança e Risco. Este roster é ponto de partida — adapte ao domínio real, mantendo as invariantes: um papel de risco com poder de bloquear, o auditor fora do fluxo, e convocação por gatilho, não por organograma.

---

## MEMÓRIA ENTRE RODADAS (o efeito plataforma)

Automatizar N esteiras é trabalho; fazer a esteira N+1 custar menos que a N porque as anteriores viraram bloco é plataforma — e essa é a métrica declarada desta skill. O squad **documenta e aprende com cada proposta**: além dos artefatos da rodada, mantém dois artefatos **contínuos**, que atravessam rodadas:

- **Catálogo de building blocks** (`T4`) — blocos de *capacidade*: o que já foi resolvido e é reaproveitável (extração, comparação, consulta).
- **Banco de precedentes** (`T6`) — blocos de *conhecimento*: o que já foi **investigado**. Cada esteira deliberada a fundo destila, no fim da rodada, uma ficha de precedente: problema-tipo decomposto em elementos, forma de solução, exceções-tipo, condições de governança recorrentes, e a coluna que dá honestidade ao reúso — **o que não transfere**. Recomendações de "não automatizar" também viram ficha: precedente negativo poupa a mesma investigação duas vezes.

Na triagem de cada rodada nova, a esteira entrante é decomposta em elementos e casada contra os dois artefatos. Um match **acelera a instrução** (os pareceristas partem do que já foi pensado), nunca a substitui.

> **TRAVA ANTI-ANCORAGEM.** O risco simétrico do reúso é a analogia forçada: aplicar um precedente porque parece, não porque é. Todo match exige **teste de aderência por escrito** — o que é igual, o que difere, o que do precedente NÃO transfere para o caso novo — e os pareceristas (o P4 em especial) mantêm o poder de derrubar a analogia. O auditor caça precedente aplicado sem teste de aderência. Um mapeamento que só lista o que serve é indistinguível de argumento de venda.

---

## FLUXO DE UMA RODADA (siga em ordem; cada fase tem porta de saída)

### FASE 0 — INTAKE (`kit/INTAKE/I01`)
≈5 perguntas ao usuário: o lote de esteiras (3–7 por rodada), o que se sabe de cada uma (volume, quem avalia hoje, dado envolvido, custo do erro), building blocks já existentes, e restrições conhecidas.

> **TRAVA DE HONESTIDADE (inegociável):** se o usuário não fornecer esteiras reais documentadas, toda esteira usada é **fictícia e rotulada como fictícia** no cabeçalho de cada artefato ("esteira hipotética, criada para demonstração"). Nunca escreva nada que se possa ler como descrição de um processo real de uma instituição específica sem fonte.

**Porta:** o lote existe por escrito, com o que se sabe e o que se assume marcado como assunção.

### FASE 1 — SCAFFOLD
Crie a pasta da rodada na área de trabalho: `{RODADA}/` com `Pareceres/`, `Auditoria/` e os templates de `kit/TEMPLATES/` como referência. Grave o lote como `{RODADA}/00-lote.md`.

### FASE 2 — TRIAGEM + CONSULTA A PRECEDENTES (barata, antes dos pareceres)
Para cada esteira do lote: (a) um parágrafo — o que é, e nota preliminar nos 5 critérios; (b) **decomposição em elementos** (tipo de dado, tipo de ato, tipo de julgamento, integração) e **consulta ao catálogo (T4) e ao banco de precedentes (T6)**. Para cada match, escreva o **teste de aderência** (igual / difere / não transfere) — matches viram insumo dos pareceres, com o teste anexado. (c) **Convocação:** verifique os gatilhos de P5/P6 (e das convocáveis) contra os elementos da esteira; registre por escrito quais cartas foram convocadas e por qual gatilho. Selecione 1–2 esteiras para deliberação profunda; as demais recebem só a linha no diagnóstico. **Não rode o rito completo para tudo** — rito aplicado a decisão de rotina é o jeito mais rápido de destruir o business case.

> **CEGAMENTO (ratificado 18-08-2026):** as notas preliminares nos 5 critérios são material do **orquestrador** (para selecionar e depois compor o diagnóstico) — **não vão aos pareceristas**. É o mesmo princípio do auditor, um degrau antes: quem opina recebe o caso, nunca o juízo prévio de quem orquestra.

**Os 5 critérios (explícitos, sempre os mesmos):**
1. **Custo do erro** — o que acontece quando a automação erra? Reversível em quanto tempo, por quem?
2. **Reversibilidade do ato** — o ato da esteira desfaz-se, ou produz consequência sobre cliente/regulador?
3. **Volume × variância** — quantos casos, e quão parecidos entre si? (Alto volume + baixa variância prioriza; alta variância pede humano.)
4. **Reaproveitamento** — parte do problema já está resolvida (building block do catálogo) ou já foi investigada (precedente do banco, com teste de aderência)? Reúso derruba o custo e sobe a prioridade.
5. **Clareza regulatória** — o terreno normativo é conhecido, ou a esteira toca área cinzenta que exigiria parecer jurídico antes de qualquer desenho?

### FASE 3 — PARECERES EM PARALELO (um subagente por carta CONVOCADA, CEGO à triagem)
Para cada esteira em deliberação profunda, spawne **um subagente por carta convocada** (mesa fixa P1–P4 + as de gatilho presentes), entregando a ele: a carta de papel (verbatim), o **lote** (o caso), o **fato da seleção** ("esta esteira foi selecionada para deliberação profunda" — sem o porquê), e os **matches de precedente com teste de aderência** (se houver). **NÃO entregue a triagem nem os escores preliminares** — o parecerista forma juízo do caso, não do juízo do orquestrador. Cada um devolve **só o parecer** no formato da carta, gravado em `{RODADA}/Pareceres/`. Economia de contexto: o subagente lê só o que a carta indica e devolve só o parecer.

### FASE 4 — DOSSIÊ (`kit/TEMPLATES/T1`)
Componha o dossiê com os **4 elementos**: pareceres, **conflitos entre eles expostos** (um dossiê em que todos concordam é sinal de papéis mal desenhados ou de desconforto editado), riscos, recomendação. A divergência é o conteúdo mais valioso — nunca a suavize.

### FASE 5 — ARTEFATOS-FIM
- **Diagnóstico priorizado** (`T2`): o lote inteiro ranqueado pelos 5 critérios, com a recomendação e o porquê em uma frase por esteira.
- **Blueprint** (`T3`): para a(s) esteira(s) priorizada(s), a especificação de skill/conector MCP — pronta para engenharia avaliar, não para rodar.
- **Catálogo de building blocks** (`T4`): o que esta rodada identificou de reaproveitável, novo ou existente.

### FASE 6 — AUDITORIA APARTADA
Spawne o auditor com o charter de `references/auditor_apartado.md` **verbatim**, anexando só: caminhos dos artefatos + ponteiro ao registro de decisões. **Não anexe sua justificativa.** Aplique os refinos antes de dar a rodada por encerrada. Veredito "precisa-retrabalho" → corrija e re-audite.

**Auditoria periódica do cânone (ratificada 18-08-2026):** as cartas de papel são o cânone que gera a deliberação — e um cânone que nunca é auditado degrada em silêncio. A cada ~3 rodadas, ou sempre que uma carta for emendada, spawne o auditor com **as próprias cartas** como artefatos (raia dele: integridade, discriminância e coerência com os templates — nunca mérito de domínio). Emenda de carta é ato estruturante: passa por ratificação humana e vira **DEC-R{n}-{nnn}** no registro.

### FASE 7 — RATIFICAÇÃO, REGISTRO E DESTILAÇÃO
Apresente ao usuário: diagnóstico + blueprint + parecer do auditor. **O usuário ratifica; o squad recomenda.** Cada decisão ratificada vira uma entrada **DEC-R{n}-{nnn}** no registro (`T5`) — registro único e contínuo da organização, com namespace de rodada no identificador (unicidade global, sem referência ambígua); número real, nunca inventado; nada se apaga (correção é nota nova). Divergência registrada com nome do papel.

Fecha a rodada a **destilação**: para cada esteira deliberada a fundo, grave/atualize a **ficha de precedente** (`T6`) — inclusive quando a recomendação foi "não automatizar" — e atualize o catálogo (`T4`). Rodada sem destilação é rodada que a organização vai pagar para refazer.

**Porta final:** os artefatos da rodada existem, auditados, com registro; catálogo e banco de precedentes atualizados; o que segue para humanos com autoridade real está explícito no blueprint (seção "o que este papel não decide").

---

## AS 4 TRAVAS (herdadas da skill-mãe; não-negociáveis)

1. **Auditor = subagente de contexto novo, charter verbatim.** Não reescreva o charter para facilitar aprovação.
2. **O auditor recebe artefatos + ponteiros — nunca o seu raciocínio.**
3. **Princípio Zero: o auditor só lê.** Se ele "quiser corrigir", está fora do papel.
4. **Ratificação é do humano.** Antes de gravar qualquer DEC estruturante, PARE e peça o "ok".

**E uma regra transversal: checklist é GATE, não conselho.** Todo checklist desta skill (das cartas P1–P4, do intake, das condições do blueprint) é **vinculante**: item sem resposta, ou respondido com evasiva, **reprova o artefato** — ele não sai. As três saídas legítimas para o que não se sabe: responder, marcar **[ASSUNÇÃO]** declarada, ou devolver para instrução com a pergunta específica. "Pulei porque era demo" não é nenhuma das três.

---

## ESCOTILHA: quando subir para o firewall pleno

Esta versão roda tudo em um projeto, com o auditor como subagente — atrito mínimo, ideal para demonstração e para rodadas exploratórias. Mas o nível de firewall do auditor não se decide pelo tamanho do projeto: **decide-se pelo risco do que está sendo avaliado.** Cinco gatilhos sobem o item para o modelo da skill irmã **`criar-estudio-robusto`** (os dois últimos ratificados em 18-08-2026, herdados dos próprios critérios de priorização):

1. Recomendação com **consequência regulatória**;
2. **Dado sensível** no escopo;
3. Blueprint que **remove revisão humana de ato sobre cliente**;
4. **Irreversibilidade alta** do ato da esteira (critério 2 invertido: quanto menos o erro se desfaz, mais firewall a avaliação merece);
5. **Reúso/raio de alcance alto** (critério 4 invertido: um building block consumido por muitas esteiras é infraestrutura load-bearing — o erro nele se propaga por todas).

Sinal adicional a considerar (não ratificado como gatilho): contexto adversarial — quando a saída vai para quem tem incentivo de contestá-la. No modo robusto: validador em **projeto separado**, sessão isolada, conectado aos artefatos em modo leitura — idealmente **outro modelo** — sem nunca compartilhar contexto com quem produz. O custo é o relay (levar cada lote ao validador); o que se compra é a separação de poderes por topologia, não por disciplina.

| | Auditor subagente (esta skill) | Validador em projeto separado (robusto) |
|---|---|---|
| Firewall | Por disciplina (4 travas) | Por topologia (sessões isoladas) |
| Atrito | Quase zero | Relay a cada lote |
| Quando | Exploração, demonstração, baixo risco | Recomendações com consequência regulatória / irreversível |

---

## LIMITES (ler antes de apresentar resultados a qualquer pessoa)

- O squad **delibera e especifica**; a automação em si é trabalho de engenharia, sob os controles da instituição — outra coisa, outro conjunto de controles.
- Nenhum dado real de cliente entra no contexto dos agentes deliberativos. Se a deliberação "precisar" de dado individual, o problema é de arquitetura, não de permissão.
- Parecer bem escrito e substantivamente errado é o custo mais provável do dia a dia; a defesa é revisão humana recorrente, não configuração.
- Esta skill nasce de arquitetura exercitada em organizações que deliberam sobre trabalho — nenhuma delas executou ato sobre cliente real sob volume. O que ela transfere é o aparato de governança da deliberação; que isso acelere uma esteira real é hipótese a testar, não resultado.

## RECURSOS
- `kit/PERSONAS/P1–P6` — as seis cartas de papel (P1–P4 mesa fixa; P5–P6 convocadas por gatilho).
- `kit/TEMPLATES/T1–T6` — dossiê · diagnóstico priorizado · blueprint · catálogo de building blocks · registro de decisões · ficha de precedente.
- `kit/INTAKE/I01` — o intake de rodada.
- `kit/EXEMPLO/` — **uma rodada completa, rodada de verdade** (esteiras fictícias rotuladas), com pareceres, dossiê, artefatos, parecer do auditor e registro. Use como âncora de profundidade e formato.
- `references/auditor_apartado.md` — o charter do auditor (passar verbatim).

---
*Adaptação de `criar-estudio-simples` (Dan/Daniel Corral) para o domínio de esteiras de dados · agosto/2026 · v1.4 (v1.1: memória entre rodadas — banco de precedentes; v1.2: DEC-R{n}, checklists vinculantes, red-team "curto-e-vago"; v1.3: cegamento, governança do catálogo, 5 gatilhos da escotilha, auditoria do cânone; v1.4, ratificada pela autoridade-fonte: mesa de 6 cartas — P5 Segurança Adversarial e P6 Dados/Avaliação por gatilho — e matriz de convocação; v1.5: segunda rodada executada sob as regras completas com devolução para instrução, blueprint da rodada 1 provado em bancada — /prototipo, 8/8 testes — e nota de escala) · preset leve (demonstração), profundidade proporcional ao risco e ao propósito — concretude, não comprimento. Variante de firewall máximo: `criar-estudio-robusto`.*
