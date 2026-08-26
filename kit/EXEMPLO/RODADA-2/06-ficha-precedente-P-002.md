# P-002 · Conciliação de registros entre dois sistemas com escrita de correção · rodada RODADA-2 · 2026-08-24
> Origem: dossiê `04-dossie-EH-B.md` · DECs R2-001…003 · **sem blueprint** (a rodada devolveu para instrução — e isso é parte do precedente)
> Rótulo da esteira de origem: **FICTÍCIA (demonstração)** · Status da recomendação de origem: **recomendação pendente de ratificação**
> Consumiu: P-001 (com teste de aderência desafiado e parcialmente corrigido pelos pareceristas) · BB-001/BB-002 em bancada.

## 1. O problema-tipo, decomposto em elementos
Dois registros estruturados do mesmo titular divergem entre sistemas internos; alguém decide qual prevalece e **escreve** a correção.
- Tipo de dado: registros estruturados internos (dado pessoal); **sem documento não estruturado**.
- Tipo de ato: **correção de registro** (escrita em sistema) — um grau acima de aprovar/reprovar; apaga a divergência, que era o único sinal de erro.
- Tipo de julgamento: comparação tolerante = determinística com score; **prevalência = regra de negócio + julgamento, fronteira desconhecida até instruir a fila**.
- Integrações: leitura em 2 sistemas + histórico + caminho de escrita com snapshot.

## 2. A forma de solução investigada
Workflow `concilia-cadastro` (loop de agente só no match ambíguo; prevalência humana na fase 1) + conectores `cadastro-read`/`cadastro-write` (condicionado) + skill `resolve-divergencia` **ainda não escrevível** (regra de prevalência não instruída) + BB-003 `compara-cadastro` como definição canônica única de comparação fuzzy.

## 3. Recomendação de origem e o porquê
**Devolver para instrução** (terceiro estado), depois sombra sem escrita com prevalência 100% humana. Variável dominante: a regra de prevalência não existe escrita e a fila nunca foi medida — e o ato escreve, com custo de erro assimétrico.

## 4. Exceções-tipo e achados operacionais
Ambas as versões erradas (mudança real não capturada); colisão de identidade / alteração legal de nome; correção bloqueada ou reaberta pela carga batch seguinte. Achados: a rajada pós-batch muda de forma com a automação (pico de casos estranhos); revisão de amostra degrada para carimbo (medir tempo por item); o **canal informal de "consertar atrás da esteira" é métrica**, não anedota.

## 5. Condições de governança recorrentes
Herdadas de P-001 e confirmadas: dono nomeado, duas trilhas, métrica de guarda + amostragem, minimização/retenção. **Novas deste problema-tipo (candidatas a recorrentes em qualquer esteira que ESCREVE):** snapshot imutável pré-escrita das versões originais; segregação em quatro (propor ≠ aprovar ≠ escrever ≠ auditar) imposta por credencial; "recência sozinha nunca decide" prevalência; proibição de "terceira versão" (a saída só pode ser idêntica a uma das entradas); gatilho objetivo de re-avaliação do limiar (banda de roteamento, discordância na amostra, mudança de schema/carga).

## 6. O QUE NÃO TRANSFERE
- A **devolução para instrução** é deste caso: esteiras com regra de decisão já escrita e fila medida não herdam o desfecho.
- A fronteira regra×julgamento da prevalência é **desta operação** — cada caso novo mede a sua.
- O corte da terceira caixa "por processo" (humano na porta de escrita via restrição de comitê) é contingente ao intake fictício — não assumir que existe em outro contexto.
- O match de **endereço** segue sem código em lugar nenhum: não citar como existente.

## 7. Gatilhos de aderência (responder antes de aplicar este precedente)
1. O ato escreve em sistema (correção/execução) — ou só classifica? Se só classifica, use P-001, não este.
2. A "regra de decisão" (prevalência ou análoga) está escrita e aprovada por dono de negócio — ou vive na cabeça de quem opera?
3. O sinal de erro sobrevive ao ato (trilha/snapshot) — ou o ato o apaga?
4. Existe adversário com incentivo a *usar* a esteira (induzir a entrada para colher a escrita)? Se sim, P5 é convocação obrigatória.
5. O score/limiar envolvido tem curva de calibração sobre a fila real — ou é heurístico de bancada?
