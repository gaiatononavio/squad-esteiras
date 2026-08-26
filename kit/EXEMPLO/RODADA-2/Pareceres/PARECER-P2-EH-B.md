# PARECER P2 · EH-B — Conferência de divergência cadastral entre dois sistemas (FICTÍCIA)

> Parecerista: P2 · Governança e Risco Operacional · RODADA-2 · 2026-08-24
> Insumos: `00-contexto.md`, `02-insumo-pareceristas.md`, ficha P-001, `prototipo/README.md`. Esteira **FICTÍCIA**.

## (1) Pergunta-assinatura
Hoje ninguém está nomeado como responsável pelo caso que passar errado — o caso não traz dono humano da esteira, e isso é achado, não detalhe. O ato final **escreve** em sistema de cadastro e é apenas **medianamente** reversível: a correção técnica é possível, mas sem trilha que preserve as duas versões pré-correção a divergência original se perde e a reversão vira reconstrução arqueológica. Portanto: reversível **só se** o desenho gravar o estado anterior antes de toda escrita — condição inegociável deste parecer.

## (2) Checklist (vinculante)

**1. Reversibilidade do ato final.** Média, e condicionada ao desenho. Reverter exige saber o valor anterior de cada campo corrigido; sem snapshot pré-escrita, irrecuperável na prática. [ASSUNÇÃO] Com snapshot: reversão por operação humana autorizada, em horas, a custo baixo — prazo, executor e procedimento não foram fornecidos e devem constar do blueprint. Concordo com o teste de aderência: a reversibilidade **alta** de P-001 (gatilho 1 da ficha) **não transfere**; herdá-la seria erro de precedente. Há ainda custo latente: registro errado propagado gera comunicação ao endereço errado antes da detecção.

**2. Dado pessoal tocado e mudança de acesso.** Nome e endereço — pessoal, não sensível (nenhum dado sensível declarado no caso). A automação muda o mapa de acessos: um componente não humano passa a **ler dois sistemas e escrever em um**, com credencial de escrita em cadastro que hoje é do analista (gatilho que convocou P5). Exigir minimização (o componente vê só os campos divergentes e o histórico estritamente necessário, não a ficha inteira) e definição de retenção da trilha — que passa a armazenar valores antigos de dado pessoal, ela própria objeto de tratamento.

**3. Segregação de funções.** No fluxo manual, um mesmo analista compara e corrige — a automação não pode reproduzir essa concentração num agente só. Condição: **propor ≠ aprovar ≠ escrever ≠ auditar**. O componente que propõe a prevalência não detém credencial de escrita; a escrita é executada por componente determinístico após aprovação; a amostragem de auditoria é feita por quem não opera a esteira.

**4. Trilha caso a caso.** Não existe hoje (o caso diz que a divergência original se perde). O desenho precisa das **duas trilhas**: deliberação (as duas versões em conflito, a regra de prevalência aplicada, evidência do histórico, score e limiar — o porquê, reconstituível meses depois) e execução (o que foi escrito, onde, quando, por qual credencial, com o estado anterior). A trilha por caso do BB-002 prova o **contrato** em bancada com dados sintéticos — não é controle operacional; não contar como implementado.

**5. Teste das três caixas.** (a) Dado privado: sim. (b) Conteúdo não confiável: atenuado — a entrada são dois registros estruturados internos, não documento de cliente (concordo com o teste de aderência: o gênero difere); mas nome/endereço são texto originalmente fornecido pelo cliente, logo não plenamente confiável. (c) Saída externa: **não há no desenho previsto** — a escrita é em sistema interno. A perna cortada é a (c), e deve ser cortada **por permissão**: credencial restrita aos campos da correção nos sistemas nomeados, nenhum canal de comunicação externa (e-mail, notificação a cliente) acoplado à esteira. Se alguém propuser "avisar o cliente automaticamente", as três caixas se fecham e este parecer reabre.

**6. Orientação não é imposição.** Condições críticas e sua garantia exigida: escrita só após aprovação humana → **trava de credencial** (o proponente não tem escrita), nunca instrução; score abaixo do piso roteia a humano → **código de workflow** (como no BB-002), não prompt; escopo de campos → **permissão no sistema**, não pedido educado. Achado central: a regra de **qual versão prevalece** (recência? sistema-fonte? histórico?) é regra de negócio nova, que EH-A não tinha — se ela for entregue como julgamento de modelo instruído por texto, é condição crítica garantida só por cooperação do modelo: achado, não mitigação. Exigir regra explícita aprovada pelo negócio, implementada deterministicamente; o que ela não cobrir cai em fila humana com o motivo na tela.

**7. Autoridade humana externa antes de qualquer piloto.** (i) Comitê interno: restrição do intake — qualquer remoção de revisão humana de ato sobre cliente passa por ele; enquanto não deliberar, todo veredito é confirmado por humano. (ii) Jurídico/compliance humano (categorias, sem citar norma de cabeça): base legal do tratamento e da correção de dado cadastral; retenção e descarte da trilha que guarda valores antigos; autenticação forte e gestão da credencial de escrita; trilha auditável com retenção definida; escopo de testes de segurança pré-piloto; e, **se** a comparação usar modelo de fornecedor externo, classificação interna do serviço e cláusulas de terceirização. Este parecer prepara essa conversa; não a substitui.

## (3) Veredito
**COM CONDIÇÕES** (não é bloqueio: nada na mesa remove revisão humana — se o blueprint vier sem C1–C3, converte-se em BLOQUEIO):
- **C1.** Snapshot pré-escrita obrigatório + duas trilhas (deliberação e execução), com retenção definida.
- **C2.** Escrita gated por aprovação humana caso a caso até deliberação do comitê; gate por credencial, não por instrução.
- **C3.** Regra de prevalência explícita, aprovada pelo dono de negócio, determinística; sem cobertura → fila humana com motivo.
- **C4.** Segregação por credencial: propor ≠ aprovar ≠ escrever ≠ auditar; dono humano nomeado no blueprint.
- **C5.** Métrica de guarda + amostragem periódica de correções aplicadas + procedimento de rollback testado — herdadas da seção 5 do P-001, que aqui **transfere**.
- **C6.** Instrução da fila real antes do piloto: volume [ASSUNÇÃO ~250/dia], taxonomia de divergências e fração resolvida "no olho" nunca medidos — não herdar números de EH-A (seção 6 da ficha).

## (4) Fila de autoridade externa (perguntas prontas)
1. **Ao comitê interno:** "Para EH-B, aprova-se piloto em que o sistema propõe a correção e o analista aprova caso a caso (nenhuma revisão humana removida), com trilha dupla e rollback? Que evidência o comitê exigirá para, no futuro, discutir escrita automática de qualquer subclasse de divergência?"
2. **A jurídico/compliance:** "Qual a base legal para a correção automatizada-assistida de nome/endereço, e por quanto tempo reter a trilha que armazena os valores pré-correção (dado pessoal)?"
3. **À segurança/controles internos:** "Que requisitos de autenticação forte e gestão de credencial valem para uma credencial não humana com escrita em cadastro, e qual o escopo mínimo de teste de segurança antes do piloto?"
4. **A terceirização (condicional):** "Se o match usar modelo de fornecedor externo, qual a classificação interna do serviço e que cláusulas contratuais incidem?"

*Toda assunção acima está marcada [ASSUNÇÃO]. Esteira e dados: FICTÍCIOS.*
