# LOTE DA RODADA · RODADA-DEMO · 2026-08-18

> ⚠️ **TODAS AS ESTEIRAS DESTE LOTE SÃO FICTÍCIAS**, criadas para demonstração da skill.
> Nenhuma descreve processo real de nenhuma instituição. Volumes, sistemas e nomes são inventados.
> Rótulo por esteira: FICTÍCIA.

## EH-A · Validação de comprovante de residência (FICTÍCIA)
O cliente envia um comprovante (conta de luz, água, telefone) por upload; um analista confere, caso a caso, se o documento é do tipo aceito, se está legível, se o nome bate com o cadastro e se a data está dentro da janela de validade; aprova, reprova ou pede reenvio.
- Volume: [ASSUNÇÃO] ~900 casos/dia.
- Dado: pessoal (nome, endereço) — não sensível na classificação típica da LGPD.
- Custo do erro hoje: aprovar comprovante inválido → cadastro com endereço errado (correspondência, prova de vínculo); reprovar válido → atrito e reenvio.
- Reversibilidade: alta — o cadastro pode ser corrigido; o ato não produz consequência externa imediata.
- Building block possivelmente reaproveitável: extração de campos de documento não estruturado (nome, endereço, data, emissor).

## EH-B · Conferência de divergência cadastral entre dois sistemas (FICTÍCIA)
Quando o nome ou endereço do mesmo cliente diverge entre o sistema de cadastro e o sistema de um produto, um analista compara as duas versões, consulta o histórico e decide qual prevalece, corrigindo o outro sistema.
- Volume: [ASSUNÇÃO] ~250 casos/dia, em rajadas após cargas batch.
- Dado: pessoal.
- Custo do erro: propagar a versão errada para os dois sistemas; retrabalho e risco de comunicação ao endereço errado.
- Reversibilidade: média — a correção é possível, mas a divergência original se perde se não houver trilha.
- Building block possivelmente reaproveitável: comparação fuzzy de nomes/endereços com score de similaridade.

## EH-C · Triagem de encerramento de conta com pendências (FICTÍCIA)
Pedido de encerramento chega; um analista verifica pendências — saldo residual, produto ativo, débito automático, e eventuais restrições (inclusive determinação judicial) — e decide se o encerramento segue, aguarda ou é negado com justificativa.
- Volume: [ASSUNÇÃO] ~120 casos/dia.
- Dado: pessoal + situações com implicação legal.
- Custo do erro: alto — encerrar conta que não podia ser encerrada (ex.: com restrição judicial) tem consequência regulatória e legal; negar indevidamente gera reclamação formal.
- Reversibilidade: baixa no pior caso — encerramento indevido não se desfaz limpo.
- Building block: consulta consolidada de pendências (hoje o analista abre 4 telas).

## Restrições declaradas no intake (fictícias, para a demonstração)
- Não existe catálogo de building blocks formal; esta rodada inaugura um.
- Qualquer mudança que remova revisão humana de ato sobre cliente passa por comitê interno (fila de aprovação humana, prazo desconhecido).

## Profundidade da rodada
Deliberação profunda: **EH-A** (1 esteira). EH-B e EH-C: triagem + linha no diagnóstico.
