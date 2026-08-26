# INSUMO AOS PARECERISTAS · RODADA-2 · 2026-08-24

> Este arquivo é o que os pareceristas recebem além do caso (`00-contexto.md`) e da própria carta.
> Conforme a regra de cegamento: contém o fato da seleção, a memória disponível e o teste de aderência do precedente — **não** contém escores nem juízos da triagem.

## Memória disponível para esta deliberação

**Building blocks existentes-em-bancada** (código real, 8/8 testes, dados sintéticos — ver `prototipo/README.md`):
- BB-001 `doc-extract`: extração de campos de comprovante sintético + score de confiança (conector MCP). Inclui a função `match_nome_tolerante` (match de nome tolerante a abreviação/acento).
- BB-002 `valida-comprovante`: workflow de validação com rotas de exceção e trilha por caso.
- BB-003 "comparação fuzzy de nome/endereço": **candidato** no catálogo, ainda não especificado — sobreposição evidente com o `match_nome_tolerante` da bancada. A sobreposição está aberta para esta rodada resolver.

**Precedente P-001** (`../RODADA-DEMO/07-ficha-precedente-P-001.md`): validação documental com cotejo contra cadastro (EH-A). Recomendação de origem: pilotar em modo sombra, precedido de instrução da fila real.

## Teste de aderência P-001 → EH-B (escrito pelo orquestrador; desafiem-no)

**O que é igual:** cotejo de nome/endereço com tolerância; dado pessoal não sensível; fila real nunca medida (a taxonomia de casos vive na cabeça do analista — o achado do P4 na R1 provavelmente se repete); condições de governança recorrentes da ficha (dono nomeado, duas trilhas, segregação, métrica de guarda + amostragem) candidatas a herdar.

**O que difere:** a entrada são **dois registros estruturados**, não documento não estruturado — a extração (núcleo do BB-001) provavelmente **não se aplica**; o que se aplica é só o componente de match. O ato final **escreve** em sistema (correção de registro), não aprova/reprova um item. Existe uma pergunta nova que EH-A não tinha: **qual versão prevalece** (recência? sistema-fonte? histórico?) — isso é regra de negócio, não similaridade.

**O que NÃO transfere (da seção 6 da ficha, aplicado):** a reversibilidade **alta** de EH-A não transfere — aqui é média, e a divergência original se perde sem trilha (gatilho de aderência 1 da ficha: reprovado em parte); o volume e a fração de exceção de EH-A não transferem (nunca medidos lá, inexistentes aqui); a clareza do terreno "comprovação cadastral" não cobre a decisão de prevalência.

**Gatilhos de aderência da ficha, respondidos:** (1) ato menos reversível que na origem — atenção redobrada; (2) parte determinística parece cobrir a comparação, mas a **prevalência** é julgamento — fração desconhecida; (3) não há documento de cliente — gênero diferente; (4) taxonomia de exceção **não medida** (de novo); (5) BB-001 existe **em bancada**, não em produção — contar como contrato provado, não como componente operacional.

## Fato da seleção
EH-B foi selecionada para deliberação profunda nesta rodada (proveniência no `00-contexto.md`). As cartas P5 e P6 foram convocadas por gatilho (credencial de escrita em sistema; score/limiar no desenho provável).
