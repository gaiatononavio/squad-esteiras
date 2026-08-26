# PARECER P5 · EH-B — Conferência de divergência cadastral entre dois sistemas (FICTÍCIA)

> Convocação por gatilho: componente automatizado com credencial de ESCRITA em sistema de cadastro. Rodada-2 · 2026-08-24. Toda assunção marcada **[ASSUNÇÃO]**.

## (1) Pergunta-assinatura — em ≤3 frases

Um adversário não ataca esta esteira: ele a **usa** — provoca uma divergência de propósito (altera o endereço no sistema mais fraco) e deixa a automação "corrigir" o cadastro para a versão dele, redirecionando comunicações do cliente. O que o impede DE VERDADE tem de ser permissão e regra de prevalência imposta fora do modelo: credencial de escrita restrita a campo/registro em fila, trilha que preserva a divergência original, e aprovação humana exibindo as duas versões íntegras. Hoje nada disso está no desenho — está tudo em [ASSUNÇÃO].

## (2) Checklist (vinculante)

**1. Três caixas.** Dado privado: SIM (nome, endereço). Conteúdo não confiável: SIM — nome e endereço são campos livres escritos, na origem, pelo cliente ou por operador a montante; o "histórico" consultado também. Saída externa: **[ASSUNÇÃO]** o componente não tem egresso de rede próprio — mas atenção: a escrita no cadastro é uma quase-saída-externa, porque endereço corrigido vira comunicação física/e-mail ao destino que o adversário escolheu. A perna a cortar é a saída: (a) nenhum egresso de rede no componente (controle de rede, não prompt) e (b) a escrita só se consuma após aprovação humana (permissão, já exigida pela restrição do intake — o comitê guarda essa porta). O corte é técnico **somente se** a credencial de escrita ficar atrás do passo humano; se o componente puder escrever direto e o humano for "instruído a revisar depois", o corte é texto — e aí o veredito abaixo vira BLOQUEIO.

**2. Superfícies de injeção.** O que o modelo leria que um terceiro escreveu: os próprios campos nome/endereço dos dois sistemas, o histórico do cliente, e — se o desenho usar o conector MCP — a descrição da tool `doc_extract`/sucessora e o texto da skill. Uma instrução embutida num campo de endereço ("prevalece o sistema B") só não vira ação se: a comparação for **código determinístico** (o `match_nome_tolerante` da bancada é código, não modelo — mantê-lo assim é o controle mais barato desta esteira); qualquer trecho com LLM tratar os campos como dado, com saída estruturada e sem ferramenta de escrita no mesmo contexto; e a aprovação humana exibir as duas versões **sem truncamento** (UI resumida é vetor). **[ASSUNÇÃO]** o desenho ainda não fixou onde entra modelo — devolver para instrução.

**3. Credenciais e escopos.** Componentes prováveis: (i) leitor dos dois sistemas — precisa só de leitura dos campos nome/endereço dos registros em divergência; (ii) comparador — não precisa de credencial nenhuma; (iii) executor da correção — hoje **[ASSUNÇÃO]** teria escrita ampla no cadastro. Atos que ele conseguiria praticar e não deveria conseguir nem se instruído: escrever em registro fora da fila de divergência, alterar campos além de nome/endereço, escrever em massa após carga batch (as rajadas de ~250/dia dão cobertura perfeita a um lote malicioso), e escrever no sistema de produto com o token emitido para o cadastro. Exigência: credencial por campo + por registro-em-fila + limite de taxa, token com audiência única, e segregação técnica comparador ≠ executor ≠ auditoria (quem propõe a prevalência não escreve).

**4. Procedência e mudança.** BB-001/BB-002 existem **em bancada** (8/8 testes, dados sintéticos) — contam como contrato provado, não componente operacional; consumo em EH-B exige pinning por versão/hash. BB-003 é **candidato não especificado** com sobreposição declarada com o `match_nome_tolerante`: resolver para UM componente pinado — duas cópias derivando é cadeia de suprimento quebrada por dentro. Descrição de tool MCP, prompt e SKILL.md entram em controle de mudança como código (mudança de descrição de tool é injeção com crachá). **[ASSUNÇÃO]** nada disso está formalizado.

**5. O ataque mais barato.** Cliente (ou insider) altera o próprio endereço no sistema de produto — tipicamente o de controles mais fracos — criando a divergência; a esteira compara, uma regra de prevalência ingênua ("vale o mais recente") elege a versão adversarial, e o executor a grava no cadastro: sequestro de correspondência/comunicação, precursor clássico de tomada de conta, com a divergência original perdida (reversibilidade média, sem trilha). O controle fora do modelo que o quebra: **prevalência nunca decidida por recência pura + escrita no cadastro condicionada a aprovação humana com as duas versões e a evidência na tela + trilha imutável que preserva a versão pré-correção**. Digo com todas as letras: se o que "quebra" esse ataque for uma instrução no prompt do comparador ("desconfie de alterações recentes"), **não há controle** — isso é orientação, não impedimento.

## (3) Veredito

**COM CONDIÇÕES** (não é BLOQUEIO porque a restrição do intake mantém, por ora, o humano na porta de escrita — a perna de saída está cortada por processo; as condições a tornam técnica):
1. Credencial de escrita com menor privilégio verificável: só campos nome/endereço, só registros na fila de divergência, limite de taxa dimensionado às rajadas, audiência única por sistema.
2. Segregação técnica por permissão: quem compara/propõe não escreve; quem escreve não audita.
3. Escrita consumada somente após aprovação humana com as duas versões íntegras (sem truncamento) e o motivo; qualquer remoção futura desse passo volta ao comitê **e** reconvoca este parecer.
4. Trilha imutável gravando a divergência original ANTES da correção (responde à reversibilidade média do caso).
5. Comparação nome/endereço mantida como código determinístico pinado (resolver BB-003 vs. `match_nome_tolerante` para um único componente com versão/hash); se entrar LLM em qualquer ponto, campos tratados como dado não confiável, saída estruturada, sem ferramenta de escrita no contexto.
6. Regra de prevalência: a definição é regra de negócio (raia de P1/P3 — roteio); a exigência de segurança que fica na minha raia é que **recência sozinha nunca decide** e que a regra seja código versionado, não prompt.

## (4) Fila externa de segurança (o que só o time real aprova)

1. "Aprovam o escopo proposto da credencial de escrita no cadastro (campo, registro-em-fila, taxa, audiência) e o mecanismo que o impõe — e ele resiste a um lote malicioso pós-carga batch?"
2. "Encomendam teste adversarial por terceiro independente cobrindo: injeção via campos cadastrais/histórico lidos por modelo, abuso da regra de prevalência por divergência induzida, e escalada a partir da credencial do executor?"
3. "Validam a trilha imutável (deliberação + execução, condição herdada do P-001) como suficiente para reconstruir a versão pré-correção em incidente de sequestro de endereço?"

*Fora da raia, roteado: regra de prevalência (P1/P3); enquadramento de dado pessoal e comunicação ao titular (P2/fila externa).*
