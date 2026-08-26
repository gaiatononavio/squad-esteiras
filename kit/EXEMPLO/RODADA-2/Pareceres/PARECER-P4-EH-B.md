# PARECER P4 · EH-B — Conferência de divergência cadastral entre dois sistemas (FICTÍCIA)

> Parecerista: P4 · Dono(a) da Esteira — voz de quem opera a conferência hoje.
> Rodada-2 · 2026-08-24 · Esteira **FICTÍCIA**. Todo dado não fornecido está marcado **[ASSUNÇÃO]**.

## (1) Pergunta-assinatura — "O que acontece com o caso que não se parece com nenhum dos que já vimos?"

Hoje ele cai no analista, que consulta histórico, às vezes liga para a área do produto, e decide "no olho" com uma taxonomia que nunca foi escrita — a proposta ainda não diz para onde esse caso vai, com que contexto, nem quem responde quando as DUAS versões estão erradas. Enquanto a regra de prevalência (recência? sistema-fonte? histórico?) não for extraída de quem decide hoje, o caso atípico não tem destino desenhado. E aqui o atípico não é rejeitado: ele **escreve** no cadastro — errar no atípico propaga a versão errada para os dois sistemas.

## (2) Checklist (vinculante)

**1. Caminho feliz e as 3 exceções mais prováveis; fração de exceção.**
Caminho feliz: divergência trivial (abreviação, acento, "R." vs "Rua"), histórico aponta claramente uma versão, correção óbvia no sistema desatualizado. Exceções mais prováveis, **[ASSUNÇÃO]** por analogia com o que a operação de cotejo cadastral costuma ver (a fila de EH-B nunca foi medida — restrição declarada no intake):
- (a) **Ambas as versões defensáveis ou ambas erradas** — cliente mudou de endereço e nenhum sistema tem a versão atual; recência não resolve porque a carga batch reordena timestamps;
- (b) **Divergência real de identidade** — não é grafia: são registros de pessoas distintas colididos, ou alteração legal de nome (casamento, decisão judicial) que um sistema recebeu e o outro não;
- (c) **Correção bloqueada ou colidida** — o sistema-alvo rejeita a escrita (trava, validação própria, caso em uso por outro processo) ou uma nova carga batch reabre a divergência recém-corrigida.
Fração de exceção: **[ASSUNÇÃO] desconhecida** — nem os ~250 casos/dia são medidos (o próprio volume é [ASSUNÇÃO]). Herdo do P-001 apenas o alerta, não o número: os 20–30% de lá **não transferem** (seção 6 da ficha), e concordo com o teste de aderência nesse ponto.

**2. Para onde vai a exceção na proposta — qual fila, com que contexto na tela?**
Não há proposta de desenho detalhada no caso — logo **não está definido**, e isso é a minha exigência nº 1. O mínimo aceitável, aprendido em EH-A (achado que a ficha registra): exceção cai em **fila humana única da própria esteira**, nunca em loop automático de "tentar de novo", com a tela mostrando: as duas versões lado a lado, o histórico consultado, o motivo tipado pelo qual a automação não decidiu, e — porque aqui o ato escreve — **o que a automação já fez ou deixou de fazer** naquele registro. Analista não pode receber um caso "meio corrigido" sem saber.

**3. O que muda na rotina de quem opera, e a reação provável.**
O analista deixa de fazer o cotejo trivial e passa a receber só o resíduo difícil + amostra dos casos auto-resolvidos para revisão. Reação provável: (i) o dia inteiro vira caso difícil — fadiga e queda de qualidade justamente onde o erro custa mais; (ii) desconfiança da escrita automática: quem corrige cadastro hoje sabe que a divergência original é a evidência, e se ela se perde (reversibilidade média, trilha não garantida), o analista fica sem matéria-prima para auditar o que a máquina fez; (iii) a rajada pós-batch muda de forma: em vez de fila longa de casos fáceis, pico curto de casos estranhos. **[ASSUNÇÃO]** Nada disso foi conversado com analista real — a restrição do intake confirma que a fila nunca foi instruída.

**4. O ganho prometido sobrevive à distribuição real fáceis × difíceis?**
Não há ganho quantificado no caso — o que já é resposta: qualquer ganho anunciado seria [ASSUNÇÃO] sobre [ASSUNÇÃO] (volume chutado × fração de exceção desconhecida). Segunda ordem: os casos fáceis (abreviação/acento) são exatamente os que o analista resolve em segundos; automatizá-los derruba o tempo médio **sem encolher a fila que dói**, que é a dos casos (a)–(c). E se a prevalência automática errar mesmo que pouco, cada erro gera retrabalho duplo (descorrigir + corrigir) e possivelmente comunicação ao endereço errado — o ganho líquido pode ser negativo antes de a taxa de erro parecer alta no dashboard.

**5. Que sinal operacional, em 30 dias de piloto, revelaria erro que o dashboard não mostra?**
- **Reincidência do mesmo cliente**: o registro corrigido volta a divergir na carga seguinte — métrica por cliente, não por caso (lição do P-001 que aqui transfere);
- **Correções "silenciosamente aceitas"**: taxa de concordância humano-máquina na amostra de auto-resolvidos caindo ao longo das semanas (analista cansado passa a carimbar) — medir tempo de revisão por item da amostra: se despencar, a revisão virou teatro;
- **O canal informal**: analista ligando para a área do produto ou abrindo chamado manual para "consertar o que a esteira fez" — se isso existir e não for métrica, o dashboard mostra sucesso enquanto a operação limpa atrás;
- **Perda da divergência original**: qualquer caso em que não se consegue reconstruir o "antes" a partir da trilha.

## (3) Vetos de irrealismo operacional

**VETO 1 — Regra de prevalência assumida sem a operação.** A premissa de que existe (ou pode existir) uma regra enunciável de qual versão prevalece **nunca foi verificada com quem decide hoje**. O teste de aderência acerta ao chamar isso de regra de negócio nova, mas subestima: **[ASSUNÇÃO]** parte das decisões de prevalência hoje é julgamento caso a caso com histórico, não regra — e ninguém sentou com ≥2 analistas para separar o que é regra do que é tino. Vira [ASSUNÇÃO] obrigatória no dossiê, ou a esteira volta para instrução da fila real.

**VETO 2 — Volume e composição da fila chutados.** ~250 casos/dia, "rajadas após batch", fração resolvida "no olho": tudo [ASSUNÇÃO] declarada, nada medido. Repetição literal do achado da R1 — e o precedente já mandava: **instrução da fila real ANTES do piloto**. Sem uma semana de tipificação da fila com a operação, qualquer desenho é engenharia sobre chute.

**VETO 3 — Tratar BB-001/`match_nome_tolerante` como componente operacional.** A bancada prova contrato com 8/8 testes **sobre dados sintéticos** — o próprio README diz que não prova acurácia sobre caso real. O match tolerante que resolve a fila de verdade (endereço com CEP trocado, nome social, colisão de homônimos) nunca viu um caso real desta esteira. Contar a bancada como "componente pronto" é premissa não verificada; no dossiê ela entra como contrato provado, esforço de adaptação **[ASSUNÇÃO] desconhecido**.

## (4) O que eu exigiria ver num piloto antes de confiar

1. **Antes de qualquer piloto**: 1–2 semanas de instrução da fila real — tipificação de ~2 semanas de casos com ≥2 analistas, separando explicitamente (i) divergência trivial, (ii) prevalência por regra enunciável, (iii) prevalência por julgamento. Sem isso, nem modo sombra.
2. **Modo sombra primeiro, sem escrita**: a esteira propõe a correção e a prevalência; o analista decide como hoje; mede-se concordância por tipo de caso. A escrita automática só entra depois — o ato escreve em cadastro, um grau acima de EH-A, e a restrição de comitê do intake se aplica.
3. **Trilha que preserva a divergência original** (antes/depois/motivo/fonte da prevalência) testada com caso de reversão real: alguém desfaz uma correção usando só a trilha, cronometrado.
4. **Fila de exceção com contexto completo na tela** (item 2 do checklist) validada por analista real, não por quem desenhou.
5. **As quatro métricas do item 5 do checklist** no painel do piloto desde o dia 1 — incluindo o canal informal de "conserto atrás da esteira" como métrica, não como anedota.

— Não julgo aqui arquitetura do match (P1), enquadramento do dado pessoal (P2) nem forma de produto (P3); onde encostei nesses temas foi só pelo efeito na operação.
