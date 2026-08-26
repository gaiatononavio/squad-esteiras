# CONTEXTO DO CASO · RODADA-2 · 2026-08-24

> ⚠️ **ESTEIRA FICTÍCIA**, herdada do lote da RODADA-DEMO (`../RODADA-DEMO/00-lote.md`). Nenhum dado descreve processo real de nenhuma instituição. Assunções marcadas [ASSUNÇÃO].
> Este arquivo é o **caso** entregue aos pareceristas. Não contém escores nem juízos da triagem (cegamento, regra v1.3).

## EH-B · Conferência de divergência cadastral entre dois sistemas (FICTÍCIA)

Quando o nome ou o endereço do mesmo cliente diverge entre o sistema de cadastro e o sistema de um produto, um analista compara as duas versões, consulta o histórico e decide qual prevalece, corrigindo o outro sistema.

- Volume: [ASSUNÇÃO] ~250 casos/dia, em rajadas após cargas batch.
- Dado: pessoal (nome, endereço).
- Custo do erro hoje: propagar a versão errada para os dois sistemas; retrabalho e risco de comunicação ao endereço errado.
- Reversibilidade: média — a correção é possível, mas a divergência original se perde se não houver trilha.
- O ato final **escreve** num sistema de cadastro (correção de registro): é um grau acima de EH-A, cujo ato era aprovar/reprovar um item.

## Restrições herdadas do intake (fictícias, para a demonstração)
- Qualquer mudança que remova revisão humana de ato sobre cliente passa por comitê interno (fila de aprovação humana, prazo desconhecido).
- Não há medição da fila real de EH-B (taxa de tipos de divergência, fração resolvida "no olho") — [ASSUNÇÃO] em tudo que depender disso.

## Fato da seleção
EH-B foi selecionada para deliberação profunda nesta rodada. Proveniência: recomendação da RODADA-DEMO ("rodada própria depois do aprendizado com EH-A", diagnóstico R1) — confirmada no intake desta rodada.
