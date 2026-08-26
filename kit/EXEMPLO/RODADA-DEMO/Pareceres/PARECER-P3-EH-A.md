# PARECER P3 · EH-A — Validação de comprovante de residência (FICTÍCIA)

> Rodada: RODADA-DEMO · 2026-08-18 · Papel: P3 — Produto, MCP e Skills
> Lote fictício; volumes e sistemas inventados. Assunções marcadas **[ASSUNÇÃO]**.

## 1. Pergunta-assinatura (≤3 frases)
Vira **combinação: workflow com loop de agente em um único ponto de julgamento, consumindo um conector MCP novo de extração de campos de documento e uma skill de decisão de conformidade**. O building block de maior reúso não é a esteira — é o conector `doc-extract` (nome, endereço, data, emissor de documento não estruturado), que EH-B e outras esteiras de cadastro podem consumir de imediato; ele muda a prioridade porque paga a si mesmo fora da EH-A. Não identifico building block **existente** a reaproveitar: o intake declara que não há catálogo formal — esta rodada inaugura um, e a EH-A entra criando dois blocks.

## 2. Checklist
1. **Forma:** workflow (determinístico) + conector MCP + skill. Descartes: *só conector MCP* — expõe capacidade mas não resolve a esteira, que exige orquestração (receber upload → extrair → decidir → devolver veredito); *só skill* — empacotaria o procedimento inteiro num agente, mais caro e menos auditável quando 3 das 4 checagens (tipo aceito, janela de data, match de nome contra cadastro) são regras determinísticas; *agente ponta a ponta* — variância moderada e enumerável não justifica julgamento em todas as etapas.
2. **Building blocks:** **consome** — nenhum existente (não há catálogo; restrição do intake). **[ASSUNÇÃO]** existe API/consulta ao cadastro para obter o nome de referência do cliente — realidade operacional a confirmar com P4. **Cria** — (a) conector MCP `doc-extract`: extração de campos de documento não estruturado, reaproveitável por EH-B (comparação cadastral) e por qualquer esteira de onboarding/documentos; (b) skill `valida-comprovante`: critérios de aceite empacotados (tipos aceitos, legibilidade, tolerância de match de nome, janela de validade), reaproveitável por canais que recebam comprovante (app, atendimento).
3. **Contrato mínimo (artefato principal, o workflow):** **entrada** — arquivo do comprovante (imagem/PDF) + id do cliente; **saída** — veredito {aprovar | reprovar | reenviar} + motivo codificado + campos extraídos + score de confiança; **erro** — {documento ilegível/corrompido, tipo não reconhecido, cadastro indisponível, confiança abaixo do piso} → cai para fila humana com o motivo, nunca falha silenciosa.
4. **Consumidor além do time:** o time de cadastro/onboarding que opera a fila hoje e, via conector `doc-extract`, qualquer equipe que processe documentos de cliente **[ASSUNÇÃO]**. Para adotar sem falar com o time: descrição de ferramenta e schema de entrada/saída publicados no conector, tabela de motivos codificados, documentação dos critérios da skill com exemplos aprovado/reprovado/reenvio, e dono nomeado com versionamento — sem isso é demo, não produto.
5. **Menor piloto:** modo sombra, sem tocar o fluxo do cliente — o workflow processa **[ASSUNÇÃO]** ~500 casos (meio dia do volume assumido de ~900/dia) em paralelo ao analista, que segue decidindo. Métrica: concordância veredito-máquina × veredito-humano, separada por classe (aprovar/reprovar/reenviar), e taxa de queda para fila humana. Critério de parada: concordância global < **[ASSUNÇÃO]** 90% ou qualquer "aprovar" da máquina que o humano reprovaria em taxa > **[ASSUNÇÃO]** 2% → revisar critérios da skill antes de qualquer conversa sobre produção.

## 3. Forma recomendada + building blocks
**Workflow determinístico com um loop de agente** (só na leitura/interpretação do documento e no match tolerante de nome; o resto é regra), **consumindo** o conector `doc-extract` (novo) e **invocando** a skill `valida-comprovante` (nova). Consome de existentes: nada — inaugura o catálogo. Cria: `doc-extract` (reúso: EH-B e esteiras de documentos) e `valida-comprovante` (reúso: canais de recepção de comprovante). Viabilidade técnica da extração é afirmação de P1, não minha; a restrição do intake (remover revisão humana de ato sobre cliente passa por comitê) significa que **qualquer desenho que auto-aprove/auto-reprove é condicionado** — o blueprint abaixo nasce com humano no circuito e a autonomia como fase posterior, sujeita ao que P2 condicionar.

## 4. Espinha do blueprint (≤10 linhas)
1. Upload chega → workflow valida formato/legibilidade básica (determinístico).
2. Conector `doc-extract` extrai nome, endereço, data, emissor + confiança (loop de agente #1).
3. Regras determinísticas: tipo de emissor aceito? data dentro da janela?
4. Match de nome extraído × cadastro (tolerante a abreviação/acento — julgamento restrito, loop #2).
5. Skill `valida-comprovante` consolida checagens → veredito proposto + motivo codificado.
6. **Fase 1 (piloto e produção inicial): veredito é recomendação; analista confirma** (respeita a restrição de comitê).
7. Qualquer erro/baixa confiança → fila humana com motivo; nada falha silencioso.
8. Log por caso: campos extraídos, regras disparadas, veredito, decisão humana final (trilha de auditoria).
9. Fase 2 (condicional a comitê + condições de P2): auto-decisão só para "aprovar" de alta confiança; reprovar/reenviar seguem com humano **[ASSUNÇÃO]** de que essa faixa existirá.
10. Donos: 1 dono do workflow, 1 dono do conector (versionado, descoberta publicada) — sem dono, não sai de demo.
