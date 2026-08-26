# PARECER P1 · EH-B — Conferência de divergência cadastral entre dois sistemas (FICTÍCIA)

> Parecerista: P1 · Arquiteto(a) de Dados e Engenharia · RODADA-2 · 2026-08-24
> Esteira **FICTÍCIA** — nenhum dado descreve processo real de nenhuma instituição.

## (1) Pergunta-assinatura — "Isso roda com os sistemas e dados que existem — ou só no slide?"

A **comparação** roda com o que existe: entrada é dois registros estruturados e o `match_nome_tolerante` da bancada (BB-001) prova o contrato de match de nome — embora match de **endereço** não exista em bancada nenhuma. A **decisão de prevalência** e a **escrita** no sistema corrigido só existem no slide: o intake não diz como se lê cada sistema, como se escreve de volta, nem qual é a regra de quem prevalece. Portanto: metade roda hoje, metade depende de integração e de regra de negócio ainda não instruídas.

## (2) Checklist (vinculante)

**1. Que dado a esteira consome, e ele está acessível de forma estruturada ou precisa de extração?**
Consome: (a) nome e endereço do mesmo cliente em dois sistemas (cadastro + produto); (b) histórico do cliente, usado na decisão de prevalência. Os dois registros são **estruturados** — não há documento, logo o núcleo de extração do BB-001 **não se aplica** (concordo com o teste de aderência nesse ponto). O que o intake não trouxe e precisa vir por instrução, não por assunção: **como** se acessa cada sistema (API? réplica? tela?), se o acesso é síncrono, e se o **histórico** é consultável de forma estruturada ou vive em telas/logs — se for tela, há uma extração escondida que ninguém especificou. [ASSUNÇÃO] provisória: leitura estruturada existe em ambos; escrita no sistema corrigido exige credencial/integração **nova** (nada na memória da rodada escreve em sistema).

**2. Determinística, de julgamento, ou híbrida?**
**Híbrida**, com fronteira diferente da de EH-A. Pede **regra**: normalização, comparação tolerante de nome/endereço, classificação do tipo de divergência (abreviação, acento, typo, mudança real), e os casos de prevalência trivialmente decidíveis por regra explícita (ex.: timestamp de atualização mais recente com fonte confiável — **se** essa regra existir e for escrita). Pede **julgamento**: a decisão de **qual versão prevalece** quando as regras não decidem — hoje isso é regra de negócio na cabeça do analista ("resolvida no olho", fração desconhecida, fila nunca medida). Desafio ao teste de aderência: ele está certo em separar prevalência de similaridade, mas subestima que **sem medição da fila não sabemos nem se a parte determinística cobre 10% ou 90%** — a fronteira regra/agente de EH-B é hoje [ASSUNÇÃO] pura, e isso por si só justifica devolver para instrução da fila antes de qualquer desenho fechado.

**3. Que building block existente resolve parte do problema? Qual parte fica de fora?**
- **BB-001**: só o componente `match_nome_tolerante` se aplica; o núcleo (extração de documento) não. Recomendação de catálogo: **resolver a sobreposição com o BB-003 extraindo o match do BB-001 para um bloco próprio** — o BB-003 "comparação fuzzy de nome/endereço" nasce daí, mas note: a bancada só prova match de **nome**; match de **endereço** (abreviações de logradouro, CEP, número/complemento) é problema distinto e ainda não tem uma linha de código.
- **BB-002**: as regras de validação de comprovante não se aplicam, mas o **padrão** — rotas de exceção tipadas, "não sei" cai em fila humana com motivo, trilha por caso — é reaproveitável como esqueleto do workflow de EH-B.
- **Fica de fora (tudo novo):** leitura dos dois sistemas, motor de regra de prevalência, **escrita** da correção com trilha, e o match de endereço. É mais do que o que se herda.
- Ressalva de status: BB-001/BB-002 são **existentes-em-bancada** (contrato provado sobre dado sintético, 8/8 testes) — não componentes operacionais. Nada da bancada prova acurácia sobre dado real, volume ou latência; a bancada não prova o que o piloto teria de provar.

**4. Modo de falha técnica mais provável — detectável automaticamente ou só humano percebe?**
O mais provável e o mais grave coincidem: **falso-positivo de prevalência** — o sistema decide com confiança pela versão errada e a **escreve**, deixando os dois sistemas consistentes-e-errados. Isso é **indetectável automaticamente por construção**: a divergência era o único sinal de que algo estava errado, e a correção o apaga. Só um humano (ou o cliente, ao receber correspondência no endereço errado) percebe. Consequência técnica na minha raia: a trilha precisa gravar **snapshot imutável das duas versões pré-correção** — sem isso não há detecção tardia nem rollback possível (a reversibilidade "média" do contexto vira baixa). Modo de falha secundário: rajadas pós-carga batch — o desenho precisa absorver pico, não vazão média. As implicações de governança da trilha são raia do P2; a credencial de escrita, do P5 (já convocado) — sinalizo e roteio.

**5. Custo por caso (ordem de grandeza).**
- **Inferência:** baixa — comparar dois registros curtos é ordem de **centavos ou menos por caso**; os casos resolvidos por regra custam ~zero. A ~250 casos/dia [ASSUNÇÃO], inferência é irrelevante no total.
- **Integração:** o custo **dominante** — dois conectores de leitura + um caminho de **escrita** em sistema de cadastro (categoria nova, inexistente na memória; provavelmente legado). Ordem de grandeza: semanas-a-meses de engenharia, contra dias para o resto.
- **Manutenção:** média e recorrente — a regra de prevalência acopla o workflow a **dois** sistemas que evoluem; cada mudança de schema ou de política cadastral exige revisão. Maior que a de EH-A, que só lia.

## (3) Classificação de viabilidade

**Viável com integração nova** — nomeadamente: (i) leitura estruturada dos dois sistemas, (ii) caminho de escrita com trilha/snapshot no sistema corrigido, (iii) especificação do BB-003 com match de endereço (o de nome já existe em bancada). **E exerço o poder de rebaixar:** qualquer recomendação de "automatizar" deve descer para **pilotar com amostra em modo sombra — sem escrita** (o sistema propõe, humano executa), precedido de **instrução da fila real** (taxonomia dos tipos de divergência e fração decidível por regra), porque a qualidade e a distribuição do dado não estão demonstradas — a fila nunca foi medida.

## (4) A única coisa que mais me preocupa

Automatizar a escrita faz desaparecer o único sinal de erro que a esteira tem — a própria divergência — de modo que todo falso-positivo nasce invisível; sem snapshot pré-correção na trilha, é erro sem detecção e sem volta.
