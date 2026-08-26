# TRIAGEM (material do ORQUESTRADOR — não vai aos pareceristas) · RODADA-2 · 2026-08-24

> Cegamento (v1.3): os escores e juízos abaixo NÃO são entregues aos pareceristas. Eles recebem só `00-contexto.md` + `02-insumo-pareceristas.md`.

## Escores preliminares de EH-B (5 critérios, qualitativos)
- C1 custo do erro: médio (propagação de versão errada; comunicação ao endereço errado)
- C2 reversibilidade: média (corrigível, mas a divergência original se perde sem trilha) — e o ato **escreve** em sistema
- C3 volume × variância: médio (~250/dia [ASSUNÇÃO]) / moderada, com rajadas batch
- C4 reaproveitamento: **alto** — match tolerante de nome existe em bancada (prototipo/), P-001 cobre boa parte da investigação, BB-003 é candidato sobreposto
- C5 clareza regulatória: clara [ASSUNÇÃO] (dado pessoal não sensível; sem área cinzenta evidente)

## Decomposição em elementos
Tipo de dado: registros estruturados de dois sistemas internos (nome/endereço; dado pessoal). **Sem documento não estruturado do cliente.**
Tipo de ato: **correção de registro** (escrita em sistema de cadastro) — decide qual versão prevalece.
Tipo de julgamento: comparação com tolerância (abreviação/acento/complemento) = determinístico com score; decidir **qual prevalece** = julgamento (recência? sistema-fonte? histórico?).
Integrações: leitura nos dois sistemas + escrita em um deles + histórico.

## Consulta à memória
- **Banco de precedentes:** match com **P-001** — teste de aderência completo em `02-insumo-pareceristas.md` (vai aos pareceristas, como manda a v1.1).
- **Catálogo:** BB-001/BB-002 **existentes-em-bancada** (nota de 24/08 no catálogo da R1); o componente relevante para EH-B é o **match tolerante de nome** (função `match_nome_tolerante` da bancada). **BB-003 (comparação fuzzy) é candidato sobreposto** — esta rodada deve resolver a sobreposição (governança do catálogo: definição canônica única; consultar antes de definir).

## Convocação (gatilhos v1.4, verificados contra os elementos)
- **P5 Segurança Adversarial: CONVOCADA.** Gatilho (c): componente automatizado com **credencial de escrita** em sistema de cadastro. (Gatilho (a)/(b) dependem do desenho — se houver loop de agente no julgamento de prevalência, reforça.)
- **P6 Ciência de Dados e Avaliação: CONVOCADA.** Gatilho: **score de similaridade + limiar** dirigindo decisão de prevalência/roteamento.
- Convocáveis (UX, resiliência, fornecedores): gatilhos ausentes no que se sabe do caso — não convocadas (registrado).

**Mesa desta rodada: P1, P2, P3, P4 + P5, P6 (6 pareceres).**
