# PARECER P4 · EH-A — Validação de comprovante de residência (FICTÍCIA)

> Emitido pelo P4 · Dono(a) da Esteira · RODADA-DEMO · 2026-08-18. Lote fictício — nenhum dado descreve operação real.

## 1. Pergunta-assinatura — "O que acontece com o caso que não se parece com nenhum dos que já vimos?"

O caso que não se parece com nada — fatura em nome do cônjuge, print de app de concessionária, boleto de condomínio, foto de tela com reflexo — hoje é resolvido "no olho" pelo analista experiente, e essa taxonomia nunca foi escrita. Se a automação só enumerar "luz, água, telefone", tudo que estiver fora vira reprovação ou pedido de reenvio automático, e o cliente legítimo entra em loop de reenvio sem nunca alcançar um humano. A proposta só é aceitável se o "não sei" do modelo cair numa fila humana explícita, com o documento e o motivo da dúvida na tela — não num "reprove e peça de novo".

## 2. Checklist

**(1) Caminho feliz e as 3 exceções mais prováveis.** Feliz: conta de luz/água/telefone legível, em nome do titular, dentro da janela de validade → aprova. Exceções mais prováveis: **(a) legibilidade/formato** — foto torta, PDF cortado, print de app da concessionária que não parece "conta"; **(b) titularidade** — comprovante em nome de terceiro (cônjuge, pai, locador), que o analista hoje resolve com regra tácita (mesmo sobrenome? declaração anexa?) nunca formalizada; **(c) tipo/data limítrofe** — documento fora da lista enumerada mas plausível (gás, internet, condomínio, contrato de aluguel) ou data na borda da janela. Fração de exceções: **[ASSUNÇÃO]** ~20–30% dos ~900 casos/dia (o próprio volume já é [ASSUNÇÃO] do lote); o lote não traz taxa de reprovação nem de reenvio — ninguém mediu.

**(2) Para onde vai a exceção?** A proposta (na forma em que chegou ao lote) **não diz** — não há desenho de fila de exceção. Exigência mínima: fila humana única de "dúvida do modelo", trabalhada pelos mesmos analistas de hoje, com tela mostrando o documento, os campos extraídos (nome, endereço, data, emissor), o dado do cadastro lado a lado e **o motivo pelo qual o modelo não decidiu**. Sem o motivo na tela, o analista refaz a análise inteira do zero e o ganho evapora. Nota do lote que reforça isso: remoção de revisão humana de ato sobre cliente passa por comitê interno com prazo desconhecido — ou seja, no curto prazo a automação **triará**, não decidirá sozinha.

**(3) O que muda na rotina de quem opera.** O analista deixa de ver 100% dos casos e passa a ver só exceções e (idealmente) uma amostra dos aprovados automáticos. Reação provável: alívio com o fim do caso trivial repetitivo, mas fadiga nova — o dia inteiro vira caso difícil, sem os fáceis que "respiram" a fila; e desconfiança se os erros do modelo caírem no colo do analista sem contexto. **[ASSUNÇÃO]** ninguém da operação foi ouvido sobre essa mudança — o lote não registra nenhuma conversa com analista real.

**(4) O ganho sobrevive à distribuição real?** Parcialmente. O modelo aprova rápido os casos fáceis — que já são os rápidos para o humano (segundos por caso). O tempo médio por caso despenca no dashboard, mas a fila humana fica 100% composta de casos difíceis, cujo tempo unitário não muda (pode até subir, por perda de ritmo). O ganho real está na **redução de headcount-hora total**, não no tempo médio — e ele só se realiza se a fração automatizável for de fato alta ([ASSUNÇÃO] ~70–80%, não verificada com dados da fila).

**(5) Sinal operacional invisível ao dashboard em 30 dias.** Três: **(a)** taxa de reenvio por cliente — se o mesmo cliente reenvia 3+ vezes, o modelo está reprovando/pedindo reenvio em loop sem rota de escape humana (o dashboard mostra "casos processados", não clientes presos); **(b)** analistas criando planilha paralela ou atalho informal para "casos que o modelo estraga" — sinal clássico de que a fila de exceção não funciona; **(c)** deriva silenciosa de aprovação indevida — endereço errado aprovado não reclama na hora (o custo aparece semanas depois, na correspondência devolvida), então só amostragem ativa dos aprovados automáticos detecta.

## 3. Vetos de irrealismo operacional

- **VETO 1 — volume e mix não verificados com a operação.** Os ~900 casos/dia já vêm marcados [ASSUNÇÃO] no lote, e não há dado algum de taxa de exceção, reprovação ou reenvio. Premissa não verificada: "a distribuição de casos é majoritariamente típica e enumerável". Deve constar como [ASSUNÇÃO] obrigatória no dossiê, com medição da fila real (2 semanas de amostra) antes de qualquer piloto.
- **VETO 2 — taxonomia de exceção inexistente.** A triagem diz "variância moderada e conhecida (tipos enumeráveis)", mas ninguém entrevistou o analista que resolve titularidade de terceiro e documento atípico no olho. Premissa não verificada: "os tipos aceitos e as regras de borda estão escritos em algum lugar". Ou se documenta a taxonomia com quem opera, ou a esteira volta para instrução.

## 4. O que eu exigiria ver num piloto antes de confiar

1. **Modo sombra primeiro**: 2 semanas com o modelo decidindo em paralelo sem efeito, comparado caso a caso com a decisão do analista — medindo concordância separada por fácil/difícil.
2. **Fila de exceção funcionando de verdade**: analista recebendo documento + campos extraídos + motivo da dúvida numa tela só; medir se o tempo do caso de exceção subiu ou caiu.
3. **Amostragem obrigatória dos aprovados automáticos** (ex.: 5%) revisada por humano, com canal para o analista devolver "o modelo errou aqui" e isso virar métrica.
4. **Métrica de cliente, não de caso**: taxa de clientes com 3+ reenvios e tempo até resolução final por cliente.
5. **Uma conversa registrada com pelo menos dois analistas da fila real** antes do go-live — sobre a taxonomia de exceção e sobre o que muda na rotina deles.
