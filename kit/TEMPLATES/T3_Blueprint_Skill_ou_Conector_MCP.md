# T3 — BLUEPRINT DE SKILL / CONECTOR MCP (pronto para engenharia AVALIAR, não para rodar)

```markdown
# BLUEPRINT · {nome do artefato} · esteira: {nome} · {RODADA}
> Rótulo da esteira-base: [FICTÍCIA — criada para demonstração | real documentada]
> Status: especificação para avaliação de engenharia. NÃO é sistema aprovado nem em construção.

## 1. Forma e justificativa
Conector MCP / skill / workflow (com loop de agente onde?) — e por que não as alternativas (1 frase cada).

## 2. Contrato
- Entrada: … (tipos, origem, o que é obrigatório)
- Saída: … (incl. o campo de confiança/qualidade, se houver — e a nota de que confiança
  reportada por modelo não é probabilidade calibrada até alguém calibrar)
- Erros e recusas: quando o artefato deve DEVOLVER o caso em vez de decidir

## 3. Building blocks e precedentes
- Consome (existentes): {bloco} → resolve {parte}
- Cria (novos, reaproveitáveis): {bloco} → reaproveitável por {quem}
- Precedentes aplicados: P-{nnn} → teste de aderência: {o que é igual / difere / não transfere}

## 4. Condições de governança (herdadas do parecer P2 — obrigatórias, não removíveis)
- … (ex.: revisão humana por amostragem de X%; métrica de guarda para o erro novo;
  trilha caso a caso; segregação: quem produz não confere)
- **Classifique cada controle** em dois eixos: momento (guide, antes do ato / sensor, depois do ato)
  e natureza (computacional-determinístico / inferencial). Regra dura: **instrução não é imposição** —
  para a condição crítica (o que o sistema NÃO pode fazer), texto no prompt é orientação; o controle
  que conta é o que independe da cooperação do modelo: permissão/credencial que não existe, trava
  fora do modelo. Diga qual condição crítica tem trava técnica e qual só tem texto.
- Se o artefato é conector MCP: **versão pinada** (SHA/digest, nunca só nome), allowlist por URL/comando
  (nome não é controle), e **mudança de descrição de tool entra em controle de mudança** — a descrição
  é prompt que dirige a seleção do modelo, logo mudá-la é mudar comportamento.

## 5. Rota da exceção (herdada do parecer P4)
Para onde vai o caso atípico, com que contexto, para qual fila humana.

## 6. Piloto mínimo
Amostra, métrica, critério de parada, duração. O menor experimento que resolve a dúvida.

## 7. O que este blueprint NÃO decide
A fila de autoridade externa: aprovações humanas (jurídico, compliance, comitê,
arquitetura) sem as quais nada disto vira piloto — cada uma com a pergunta já formulada.

## 8. Esforço e custo (ordem de grandeza, honesta)
Integração / inferência por caso / manutenção. "Não medido" é resposta aceitável; número inventado, não.
```
