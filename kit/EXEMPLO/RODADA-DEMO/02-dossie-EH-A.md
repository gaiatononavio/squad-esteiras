# DOSSIÊ · EH-A — Validação de comprovante de residência · RODADA-DEMO
> Rótulo: **FICTÍCIA — criada para demonstração.** Nenhum dado descreve processo real de nenhuma instituição.
> Data: 2026-08-18 · Pareceres na íntegra em `Pareceres/`.

## 1. A esteira em um parágrafo
Cliente envia comprovante por upload; analista confere caso a caso (tipo aceito, legibilidade, nome × cadastro, data na janela) e aprova, reprova ou pede reenvio. Volume [ASSUNÇÃO] ~900 casos/dia; dado pessoal não sensível; erro barato e reversível — mas o lote não traz taxa de exceção, de reprovação nem de reenvio: **ninguém mediu a fila real** (achado do P4 que atravessa o dossiê inteiro).

## 2. Pareceres — o essencial
- **P1 Arquitetura/Engenharia:** *viável com integração nova* (a consulta estruturada ao cadastro é a lacuna nº 1); tarefa híbrida — regras para tipo/data/match exato, julgamento só para legibilidade e grafia. Rebaixou para **pilotar com amostra**: a qualidade do dado não está demonstrada. Modo de falha dominante: extração confiante e errada em documento ruim.
- **P2 Governança/Risco:** **COM CONDIÇÕES** (sem bloqueio: ato reversível e fila de comitê já prevista). Achado central: **ninguém está nomeado como responsável pelo caso decidido por agente**. Seis condições, incl. duas trilhas (deliberação + execução), segregação extração ≠ decisão ≠ auditoria, métrica de guarda com amostragem e rollback.
- **P3 Produto/MCP/Skills:** forma = **workflow determinístico com loop de agente em 2 pontos** (leitura do documento; match tolerante de nome), consumindo um conector MCP novo `doc-extract` e uma skill `valida-comprovante`. Nada existente a consumir — a rodada inaugura o catálogo. O maior valor não é a esteira: é o `doc-extract`, reaproveitável por EH-B e esteiras de documentos.
- **P4 Dono da Esteira:** **dois vetos de irrealismo** (abaixo). Exceções prováveis: legibilidade, titularidade de terceiro (regra tácita nunca escrita), tipo/data limítrofe — fração [ASSUNÇÃO] ~20–30%. Exigência inegociável: o "não sei" do modelo cai em fila humana com documento + campos + **motivo da dúvida na tela**, nunca em loop de reenvio automático.

## 3. Conflitos entre pareceres — EXPOSTOS
1. **P1 × P3, sobre o chão da proposta.** P3 desenha a solução inteira em torno do `doc-extract`; P1 aponta que esse bloco **ainda não existe como componente testado** — "contar com ele como pronto seria otimismo". O blueprint herda a tensão: a peça de maior reúso é também a de acurácia não medida. Não é conflito resolvível por argumento — só por medição (piloto sombra).
2. **Triagem/P3 × P4, sobre a variância.** A triagem classificou a variância como "moderada e conhecida (tipos enumeráveis)"; o P4 vetou exatamente essa premissa: a taxonomia real de exceção vive na cabeça do analista e nunca foi escrita. Se o P4 estiver certo, a fração automatizável cai e o ganho encolhe. **A triagem fica corrigida pelo veto**: variância = [ASSUNÇÃO] até a taxonomia ser documentada com quem opera.
3. **O ganho prometido × a distribuição dos casos (P4 contra o entusiasmo geral).** O modelo aprova rápido os fáceis — que já são os rápidos para o humano. Tempo médio despenca no dashboard; a fila humana fica 100% difícil e não encolhe no tempo unitário. O ganho verdadeiro é headcount-hora total, e só se realiza se a fração automatizável for alta — que é justamente a [ASSUNÇÃO] não verificada do conflito 2.

## 4. Riscos (os que importam)
1. **Extração confiante e errada** (P1): campo sai preenchido e o cotejo "decide" sobre dado falso. Sinal: divergência na amostragem dos aprovados. Mitigação: piso de confiança que roteia a humano + amostragem contínua.
2. **Cliente preso em loop de reenvio** (P4): reprovação automática sem rota de escape humana. Sinal: clientes com 3+ reenvios. Mitigação: fila de exceção com motivo na tela; métrica por cliente, não por caso.
3. **Responsabilidade órfã** (P2): ato automatizado sem dono humano nomeado. Sinal: a pergunta "quem responde?" sem resposta em reunião. Mitigação: condição 1 do P2 — sem dono, sem piloto.
4. **Deriva silenciosa de aprovação indevida** (P4): endereço errado não reclama na hora; o custo aparece semanas depois. Sem amostragem ativa, invisível. Mitigação: amostra obrigatória de aprovados automáticos.
5. **Catálogo natimorto** (P3): `doc-extract` nasce sem dono/versionamento e vira demo. Mitigação: dono nomeado e descoberta publicada como condição do blueprint.

## 5. Recomendação
**Pilotar com amostra (modo sombra), precedido de instrução da fila real** — não "automatizar" ainda. Sequência: (a) 2 semanas medindo a fila real (volume, mix, taxa de exceção) e documentando a taxonomia de exceção com ≥2 analistas (resolve os vetos do P4); (b) piloto sombra de 2 semanas, modelo decidindo em paralelo sem efeito, concordância medida por classe (métricas de P3 e P4); (c) só então, blueprint à fila do comitê para qualquer autonomia parcial. As 6 condições do P2 entram no blueprint como não-removíveis.

## 6. O que segue para autoridade humana
Fila externa formulada pelo P2 (perguntas prontas no parecer): comitê interno (remoção de revisão humana caso a caso), jurídico/compliance (base legal e retenção da imagem — este dossiê **não** substitui essa análise), segurança/compliance (se a extração envolver terceiro).

---
**Nota de harmonização (append-only, 2026-08-18, por refino opcional da auditoria):** o §1 do parecer P3 fala em "um único ponto de julgamento" e a espinha do mesmo parecer desenha **dois** loops de agente (extração; match tolerante de nome). Este dossiê e o blueprint adotam a espinha (2 pontos), que é a versão operacional do próprio P3.
