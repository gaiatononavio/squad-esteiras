# BLUEPRINT · workflow `valida-comprovante` + conector MCP `doc-extract` · esteira EH-A · RODADA-DEMO
> Rótulo da esteira-base: **FICTÍCIA — criada para demonstração.**
> Status: **especificação para avaliação de engenharia. NÃO é sistema aprovado nem em construção.**
> Data: 2026-08-18 · Fontes: pareceres P1–P4 e dossiê da rodada.

## 1. Forma e justificativa
**Workflow determinístico com loop de agente em 2 pontos** (leitura/extração do documento; match tolerante de nome), consumindo o conector MCP `doc-extract` e invocando a skill `valida-comprovante`. Descartes: só conector MCP — expõe capacidade, não resolve a orquestração; só skill/agente ponta a ponta — 3 das 4 checagens são regra determinística, agente em tudo é mais caro e menos auditável; RPA puro — a leitura de documento não estruturado exige julgamento.

## 2. Contrato (artefato principal: o workflow)
- **Entrada:** arquivo do comprovante (imagem/PDF) + id do cliente.
- **Saída:** veredito proposto {aprovar | reprovar | reenviar} + motivo codificado + campos extraídos (nome, endereço, data, emissor) + score de confiança. *Confiança reportada por modelo não é probabilidade calibrada de acerto até alguém calibrá-la — trate como sinal de roteamento, não como medida (parecer P1).*
- **Erros e recusas:** {ilegível/corrompido, tipo não reconhecido, cadastro indisponível, confiança abaixo do piso} → o caso é **DEVOLVIDO à fila humana com o motivo da dúvida na tela** — nunca decidido, nunca falha silenciosa, nunca loop de reenvio automático.

## 3. Building blocks
- **Consome (existentes):** nenhum — o catálogo nasce nesta rodada (restrição do intake).
- **Cria:** **BB-001 `doc-extract`** (conector MCP: campos de documento não estruturado → reúso imediato por EH-B e esteiras de documentos) · **BB-002 `valida-comprovante`** (skill: critérios de aceite empacotados → reúso por canais que recebem comprovante).

## 4. Condições de governança (herdadas do parecer P2 — obrigatórias, não removíveis)
1. **Dono humano nomeado**, que responde pelos casos decididos com apoio do sistema.
2. **Duas trilhas** antes do 1º caso real: registro de deliberação por caso (campos, regras, limiares, versão) + log de execução.
3. **Segregação:** extração ≠ decisão ≠ auditoria; nenhuma etapa confere o próprio produto.
4. **Métrica de guarda + amostragem:** taxa de erro tolerada declarada; revisão humana de [ASSUNÇÃO] 5% dos aprovados automáticos; gatilho de rollback para revisão 100% humana.
5. **Fase 1 sempre com humano confirmando** o veredito proposto; autonomia parcial só após comitê (seção 7).
6. **Minimização e retenção:** extrair só os campos necessários; retenção da imagem definida com jurídico; nenhum reúso fora da finalidade cadastral.

## 5. Rota da exceção (herdada do parecer P4)
Fila humana única de "dúvida do modelo", operada pelos analistas de hoje, com tela mostrando: documento + campos extraídos + dado do cadastro lado a lado + **motivo pelo qual o modelo não decidiu**. Métrica por cliente (3+ reenvios = alarme), não só por caso. **Canal de devolução do analista** (exigência 3 do P4, incorporada por refino da auditoria): botão/rota explícita de "o modelo errou aqui", e cada devolução contabilizada como métrica do piloto — não como desabafo perdido.

## 6. Piloto mínimo (sequência acordada no dossiê)
1. **Instrução da fila real (2 semanas):** medir volume, mix e taxa de exceção; conversa registrada com ≥2 analistas da fila cobrindo **a taxonomia de exceção E o que muda na rotina deles** (resolve os vetos do P4; escopo da conversa corrigido por refino da auditoria).
2. **Modo sombra (2 semanas):** workflow decide em paralelo, sem efeito; concordância máquina × humano medida por classe (aprovar/reprovar/reenviar) e por fácil/difícil.
3. **Critérios de parada** [ASSUNÇÃO, a calibrar no passo 1]: concordância global < 90%, ou "aprovar" da máquina que o humano reprovaria > 2% → revisar critérios antes de qualquer conversa de produção.

## 7. O que este blueprint NÃO decide (fila de autoridade humana)
- **Comitê interno:** aprovar qualquer decisão sem humano caso a caso ("aprovamos autonomia para a classe 'aprovar' de alta confiança, dado métrica de guarda X, amostragem Y, rollback Z — sim/não/com que limites?").
- **Jurídico/Compliance:** base legal da extração automatizada e retenção máxima da imagem — este blueprint não substitui essa análise.
- **Segurança/Compliance:** se a extração processar documento fora do ambiente da instituição, sob que contrato e controles.
- **Arquitetura/Engenharia:** avaliação desta especificação, incl. a integração com o cadastro (lacuna nº 1 do P1).

## 8. Esforço e custo (ordem de grandeza, honesta)
- **Inferência:** centavos por documento; a ~900 casos/dia [ASSUNÇÃO], dezenas de reais/dia — irrelevante frente ao custo de analista (P1).
- **Integração:** o custo dominante — consulta estruturada ao cadastro + gancho no fluxo de reenvio. **Não medido.**
- **Manutenção:** baixa–média — novos layouts de emissor e mudanças na lista de aceitos exigem revisão periódica, sob o dono nomeado.
- **Construção do piloto:** não medida. "Não medido" é resposta aceitável; número inventado, não.
