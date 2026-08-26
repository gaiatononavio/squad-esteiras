# DOSSIÊ · EH-B — Conferência de divergência cadastral · RODADA-2
> Rótulo: **FICTÍCIA — criada para demonstração.** Data: 2026-08-24 · Pareceres na íntegra em `Pareceres/`.

## 1. A esteira em um parágrafo
Nome/endereço do mesmo cliente divergem entre dois sistemas; analista compara, consulta histórico e decide qual versão prevalece, **corrigindo (escrevendo) no outro sistema**. Volume [ASSUNÇÃO] ~250/dia em rajadas pós-batch; dado pessoal; reversibilidade média — e a divergência original, que é o único sinal de erro, se perde sem trilha. Fila real nunca medida.

## 2. Convocação e pareceres
Cartas convocadas: **P1–P4 (mesa fixa) + P5 (gatilho: credencial de escrita em cadastro) + P6 (gatilho: score/limiar de similaridade)** — registro da convocação em `01-triagem-orquestrador.md`. Pareceristas cegos à triagem (instrução de spawn registrada em `03-instrucao-de-spawn.md`).

- **P1 Arquitetura/Engenharia:** *viável com integração nova* (leitura dos 2 sistemas, caminho de escrita com snapshot, match de endereço inexistente); rebaixou para **sombra sem escrita, precedida de instrução da fila**. Achado central: **a correção apaga o único sinal de erro** — falso-positivo de prevalência nasce invisível; snapshot pré-correção imutável é condição de detecção e rollback.
- **P2 Governança/Risco:** **COM CONDIÇÕES C1–C6** (vira BLOQUEIO se o blueprint vier sem snapshot, gate humano por credencial e regra de prevalência explícita). Segregação em quatro: **propor ≠ aprovar ≠ escrever ≠ auditar**. A reversibilidade alta do P-001 **não transfere** (herdá-la seria erro de precedente).
- **P3 Produto/MCP/Skills:** forma = workflow `concilia-cadastro` + conectores `cadastro-read` e `cadastro-write` (condicionado) + skill `resolve-divergencia` — **que hoje não pode ser escrita**: a regra de prevalência não está instruída (devolução para instrução). Resolveu a sobreposição do catálogo: **BB-003 `compara-cadastro` como definição canônica única**, absorvendo o `match_nome_tolerante` da bancada, com BB-001 refatorado para consumi-lo.
- **P4 Dono da Esteira:** **três vetos** (abaixo). Exceções-tipo: ambas as versões erradas; colisão de identidade/alteração legal de nome; correção bloqueada ou reaberta pela carga seguinte. Sinais invisíveis ao dashboard: reincidência por cliente, revisão que vira carimbo (medir tempo por item da amostra), e o **canal informal de "consertar o que a esteira fez"** como métrica, não anedota.
- **P5 Segurança Adversarial (convocada):** **COM CONDIÇÕES**; o ataque mais barato é o adversário **usar** a esteira: induzir divergência no sistema mais fraco e deixar a prevalência por recência gravar a versão dele no cadastro (sequestro de comunicação). Regras: **recência sozinha nunca decide**; escrita atrás de aprovação humana **por credencial** (se for por instrução, vira BLOQUEIO); comparação mantida como código determinístico pinado.
- **P6 Dados/Avaliação (convocada):** **os números não sustentam** automação — o score da bancada é heurístico e não calibrado (não carrega decisão de escrita), a regra de prevalência não tem base histórica, e não existe gatilho de degradação. Rebaixou para "no máximo sombra, precedida de instrução; prevalência 100% humana". Teste mais importante se houver LLM: **proibição de "terceira versão" alucinada** — a saída só pode ser idêntica a uma das duas entradas.

## 3. Conflitos e divergências — EXPOSTOS
1. **P5 × padrão do blueprint EH-A, sobre modelo no match.** P5 exige a comparação como **código determinístico pinado** (o controle mais barato da esteira); o padrão herdado de EH-A contempla modelo atrás do mesmo contrato, e P6 já desenhou a bateria para esse caso. Não resolvido por argumento: fica como decisão explícita do desenho (default desta rodada: determinístico; LLM só com a bateria do P6 e as travas do P5).
2. **P2 × P5, sobre a segunda caixa.** P2 classificou "conteúdo não confiável" como *atenuado* (registros internos estruturados); P5 como *presente* (nome/endereço são, na origem, texto do cliente). Divergência nominal mantida — a leitura do P5 é a mais conservadora e é a adotada na recomendação.
3. **Todos × o teste de aderência do orquestrador.** O teste sobreviveu no essencial (extração não se aplica; reversibilidade alta não transfere), mas foi **corrigido em dois pontos** por quem tinha o dever de desafiá-lo: P1/P4 — ele subestima que, sem medição da fila, nem a fronteira regra×julgamento da prevalência é conhecida; P6 — "contrato provado ≠ número provado" (os 8/8 testes provam rotas, não taxas).

## 4. Riscos (os que importam)
1. **Erro que apaga a própria evidência** (P1): sistemas consistentes-e-errados; sem snapshot pré-correção, sem detecção nem volta.
2. **Sequestro de endereço por divergência induzida** (P5): prevalência ingênua por recência vira ferramenta do adversário.
3. **Prevalência inventada** (P4-veto 1 / P3): regra de negócio que ninguém extraiu da operação; automatizá-la é engenharia sobre chute.
4. **Score sem procedência decidindo escrita** (P6): limiar sobre distribuição desconhecida, sem gatilho de re-avaliação.
5. **Revisão que vira teatro** (P4): analista cansado carimbando a amostra — medir tempo de revisão por item desde o dia 1.

## 5. Recomendação
**Devolver para instrução (o "terceiro estado": não aprova, não mata), com as perguntas específicas:** (a) instrução da fila real — 1–2 semanas de tipificação com ≥2 analistas, separando divergência trivial × prevalência por regra enunciável × prevalência por julgamento; (b) explicitação da regra de prevalência pelo dono de negócio (o que ela não cobrir permanece humano); (c) base histórica mínima de "qual versão estava certa". Só então: **piloto sombra sem escrita** (a esteira propõe, o analista decide), com prevalência 100% humana, as condições C1–C6 do P2 e as 6 do P5 no desenho, e os sinais do P4 no painel desde o dia 1. Paralelamente, **promover BB-003 a definição canônica única** (proposta do P3) — o reúso desta rodada.

## 6. O que segue para autoridade humana
Perguntas prontas nos pareceres: comitê interno (P2-1), jurídico/compliance (P2-2: base legal da correção e retenção da trilha com valores antigos), segurança (P2-3 + as 3 do P5, incl. teste adversarial por terceiro), validação de modelo (as 3 do P6, incl. sinalização de equidade por estrato de nome), terceirização condicional (P2-4).
