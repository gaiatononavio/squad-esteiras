# PARECER P2 · EH-A — Validação de comprovante de residência (FICTÍCIA)

> Rodada: RODADA-DEMO · 2026-08-18 · Papel: P2 — Governança e Risco Operacional
> Base: `00-lote.md` e `01-triagem.md`. Esteira fictícia; dados não fornecidos pelo lote marcados **[ASSUNÇÃO]**.

## 1. Pergunta-assinatura — "Quem responde pelo caso que passar errado, e o ato é reversível?"

O ato (aprovar/reprovar/pedir reenvio de comprovante) é reversível: o cadastro pode ser corrigido e não há consequência externa imediata, segundo o próprio lote. Quem responde, porém, **não está nomeado em lugar nenhum do lote**: hoje é o analista caso a caso, e a proposta de automação ainda não diz quem assume a responsabilidade pelo caso decidido por agente — este é o achado central deste parecer. Antes de qualquer piloto, o blueprint precisa nomear um dono humano do processo que responda pelos atos automatizados, inclusive perante o cliente que recebeu correspondência no endereço errado.

## 2. Checklist

1. **Reversibilidade do ato final.** Alta (declarada no lote): corrigir o cadastro desfaz o erro. Ressalvas: (a) custo de reversão não é zero — o erro só se desfaz quando **detectado**, e o lote não descreve mecanismo de detecção; (b) **[ASSUNÇÃO]** enquanto não detectado, o endereço errado pode servir de prova de vínculo ou destino de correspondência, produzindo efeito externo antes da correção. Prazo/custo/responsável pela reversão: não definidos no lote — devem constar do blueprint.
2. **Dado pessoal tocado.** Nome e endereço — pessoal, não sensível na classificação típica (conforme lote). A automação muda o acesso: hoje o documento é visto por um analista; com extração automatizada, o conteúdo passa por um serviço de extração e possivelmente por logs/base de treino. Condições: minimização (extrair só os campos necessários), retenção definida para imagem e campos extraídos, e proibição de reúso do documento para outra finalidade sem nova base legal. **[ASSUNÇÃO]** a extração roda em ambiente sob controle da instituição; se envolver terceiro/nuvem externa, isso entra na fila de compliance humano.
3. **Segregação de funções.** Risco concreto no desenho ingênuo: o mesmo agente que extrai os campos **não pode** ser quem confere e aprova — quem produz não aprova. O blueprint deve separar extração (produção) de decisão (conferência), e a auditoria/amostragem não pode ser executada pelo mesmo agente que decide. **[ASSUNÇÃO]** o desenho pretendido ainda não define essa separação, pois o lote só nomeia o building block de extração.
4. **Trilha caso a caso.** Não existe no lote. Exigem-se **duas trilhas**: (i) registro de deliberação — por que este comprovante foi aprovado/reprovado (campos extraídos, regras aplicadas, limiares, versão do modelo/regra); (ii) log de execução — o que rodou, quando, com que resultado. O produto precisa das duas para responder, meses depois, por que aquele caso foi decidido daquele jeito. Reprovações e pedidos de reenvio também entram na trilha — atrito com cliente é ato relevante.
5. **Autoridade humana externa ao squad.** O intake declara: qualquer remoção de revisão humana de ato sobre cliente passa por comitê interno. Logo, qualquer variante da esteira que decida sem humano no caso a caso **depende dessa fila antes do piloto**. Perguntas prontas na seção 4.

## 3. Veredito: **COM CONDIÇÕES**

Não é BLOQUEIO: o ato é reversível e o lote prevê fila de comitê para remoção de revisão humana. Condições para a esteira seguir a blueprint/piloto:

1. **Dono nomeado**: um responsável humano pelo processo, que responde pelos casos decididos por agente.
2. **Duas trilhas desenhadas** (deliberação + execução), reconstituíveis caso a caso, antes do primeiro caso real.
3. **Segregação no desenho**: extração ≠ decisão ≠ auditoria; nenhuma etapa confere o próprio produto.
4. **Métrica de guarda + revisão por amostragem** definidas no blueprint (taxa de erro tolerada, amostra humana periódica, gatilho de rollback para revisão 100% humana).
5. **Piloto em modo sombra ou com humano confirmando**, até a passagem pelo comitê interno para qualquer decisão autônoma.
6. **Minimização e retenção** de imagem e campos extraídos definidas; nenhum reúso do documento fora da finalidade cadastral.

## 4. Fila de autoridade externa (só humanos aprovam)

- **Comitê interno (obrigatório pelo intake):** "Aprovamos que a decisão de aprovar/reprovar comprovante seja tomada por agente sem revisão humana caso a caso, dado que o blueprint prevê métrica de guarda X, amostragem Y e rollback Z — sim ou não, e com que limites?"
- **Jurídico/Compliance (LGPD):** "A extração automatizada de nome/endereço de documento enviado pelo cliente cabe na base legal já usada para a validação manual, ou exige atualização de aviso de privacidade/registro de operações? Qual retenção máxima para a imagem do comprovante?" — este parecer **não** substitui essa análise.
- **Compliance/Segurança (se houver terceiro):** "O serviço de extração processa o documento fora do ambiente da instituição? Se sim, sob que contrato e controles?" **[ASSUNÇÃO]** pergunta condicional, pois o lote não define a arquitetura.

*Parecer P2 emitido para preparar a conversa com a segunda linha de defesa real — não a dispensa.*
