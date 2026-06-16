# TODO da Entrega

Checklist operacional para acompanhar a entrega do projeto "Pull, Otimizacao e Avaliacao de Prompts com LangChain e LangSmith".

## Preparacao

- [x] Obter o link do repositorio boilerplate/template do desafio.
- [x] Fazer fork do repositorio base.
- [x] Clonar ou organizar o projeto nesta pasta.
- [x] Confirmar que a estrutura obrigatoria do projeto existe.
- [x] Criar `AGENTS.md` com o fluxo de trabalho educacional e contexto persistente do projeto.
- [x] Criar ambiente virtual Python.
- [x] Ativar ambiente virtual.
- [x] Instalar dependencias com `pip install -r requirements.txt`.
- [x] Criar API Key da OpenAI ou da Google Gemini.
- [x] Criar ou configurar conta/API Key do LangSmith.
- [x] Configurar variaveis no `.env` com base no `.env.example`.
- [x] Configurar suporte alternativo ao OpenCode Go com `deepseek-v4-flash` para evitar limite do Gemini gratuito.

## Pull do Prompt Inicial

- [x] Revisar o esqueleto de `src/pull_prompts.py`.
- [x] Implementar conexão com LangSmith usando credenciais do `.env`.
- [x] Implementar pull do prompt `leonanluppi/bug_to_user_story_v1`.
- [x] Salvar o prompt em `prompts/bug_to_user_story_v1.yml`.
- [x] Executar `python -m src.pull_prompts`.
- [x] Validar que `prompts/bug_to_user_story_v1.yml` foi criado corretamente.
- [x] Remover teste unitário extra do fluxo de pull, pois não é requisito obrigatório da entrega.
- [x] Confirmar que `pytest -q` passa após a implementação do pull.

## Analise do Prompt v1

- [x] Ler `prompts/bug_to_user_story_v1.yml`.
- [x] Identificar problemas de clareza, contexto, persona e formato.
- [x] Identificar lacunas de regras, edge cases e exemplos.
- [x] Registrar os principais problemas para documentar no `README.md`.

## Criacao do Prompt Otimizado v2

- [x] Criar `prompts/bug_to_user_story_v2.yml`.
- [x] Definir System Prompt adequado.
- [x] Definir User Prompt adequado.
- [x] Incluir persona clara, por exemplo Product Manager ou especialista em requisitos.
- [x] Incluir instrucoes claras e especificas.
- [x] Incluir regras explicitas de comportamento.
- [x] Incluir formato de saida esperado em Markdown ou User Story padrao.
- [x] Incluir Few-shot Learning com exemplos de entrada e saida.
- [x] Aplicar pelo menos uma tecnica adicional alem de Few-shot.
- [x] Registrar no YAML os metadados com pelo menos 2 tecnicas utilizadas.
- [x] Incluir tratamento de edge cases.
- [x] Garantir que nao exista nenhum `[TODO]` no prompt.

## Tecnicas de Prompt Engineering

- [x] Escolher tecnica obrigatoria: Few-shot Learning.
- [x] Escolher pelo menos uma tecnica adicional.
- [x] Avaliar uso de Role Prompting. (ESCOLHIDA)
- [x] Avaliar uso de Chain of Thought. (não escolhida)
- [x] Avaliar uso de Skeleton of Thought. (ESCOLHIDA)
- [ ] Avaliar uso de Tree of Thought.
- [ ] Avaliar uso de ReAct.
- [x] Documentar no `README.md` quais tecnicas foram escolhidas.
- [x] Documentar no `README.md` por que cada tecnica foi escolhida.
- [x] Documentar no `README.md` exemplos praticos de aplicacao das tecnicas.

## Push para LangSmith

- [x] Revisar o esqueleto de `src/push_prompts.py`.
- [x] Implementar leitura de `prompts/bug_to_user_story_v2.yml`.
- [x] Implementar push para `{seu_username}/bug_to_user_story_v2`.
- [x] Adicionar tags ao prompt publicado.
- [x] Adicionar descricao ao prompt publicado.
- [x] Adicionar metadados com tecnicas utilizadas.
- [x] Executar `python src/push_prompts.py`.
- [x] Verificar no dashboard do LangSmith se o prompt foi publicado. (Evidencia: `evidencias/06-langsmith-prompt-v2-publico.png`)
- [x] Deixar o prompt publico no LangSmith.

## Avaliacao e Iteracoes

- [x] Executar `python src/evaluate.py`.
- [x] Registrar resultados da primeira avaliacao.
- [x] Verificar Helpfulness >= 0.8. (Iteracao 2: 0.95)
- [x] Verificar Correctness >= 0.8. (Iteracao 2: 0.92)
- [x] Verificar F1-Score >= 0.8. (Iteracao 2: 0.87)
- [x] Verificar Clarity >= 0.8. (Iteracao 2: 0.95)
- [x] Verificar Precision >= 0.8. (Iteracao 2: 0.96)
- [x] Verificar media das 5 metricas >= 0.8. (Iteracao 2: 0.9298)
- [x] Identificar metricas abaixo de 0.8. (F1-Score e Clarity)
- [x] Ajustar prompt com base nas metricas baixas. (Iteracao 2: reforco de recall, estrutura por complexidade e secoes tecnicas)
- [x] Fazer novo push do prompt otimizado.
- [x] Executar nova avaliacao.
- [x] Repetir por 3 a 5 iteracoes, se necessario. (Criterio de parada atingido na Iteracao 2)
- [x] Confirmar que todas as 5 metricas ficaram >= 0.8.

## Testes de Validacao

- [x] Editar `tests/test_prompts.py`.
- [x] Implementar `test_prompt_has_system_prompt`.
- [x] Implementar `test_prompt_has_role_definition`.
- [x] Implementar `test_prompt_mentions_format`.
- [x] Implementar `test_prompt_has_few_shot_examples`.
- [x] Implementar `test_prompt_no_todos`.
- [x] Implementar `test_minimum_techniques`.
- [x] Executar `pytest tests/test_prompts.py`.
- [x] Corrigir falhas de teste, se houver.
- [x] Confirmar que todos os testes passam.

## README.md

- [x] Atualizar README.md com visao geral do projeto.
- [x] Criar secao "Tecnicas Aplicadas (Fase 2)".
- [x] Explicar as tecnicas avancadas escolhidas.
- [x] Justificar a escolha de cada tecnica.
- [x] Incluir exemplos praticos de aplicacao.
- [x] Criar secao "Resultados Finais".
- [ ] Inserir link publico do dashboard LangSmith. (README contem link do projeto e screenshots; compartilhamento publico do dashboard ainda nao confirmado)
- [x] Inserir screenshots das avaliacoes.
- [x] Criar tabela comparativa v1 versus v2.
- [x] Criar secao "Como Executar".
- [x] Documentar pre-requisitos e dependencias.
- [x] Documentar comandos para pull, push, avaliacao e testes.
- [x] Documentar configuracao do provider alternativo OpenCode Go no README.md.

## Evidencias LangSmith

- [ ] Publicar ou obter link publico do dashboard LangSmith.
- [x] Garantir que o dataset de avaliacao com 15 exemplos esteja visivel. (Evidencia: `evidencias/05-langsmith-dataset-15-exemplos.png`)
- [x] Garantir que as execucoes do prompt v2 estejam visiveis. (Evidencias: `evidencias/04-langsmith-projeto-traces.png` e links publicos dos 3 traces no `README.md`)
- [x] Garantir que as notas >= 0.8 estejam visiveis. (Iteracao 2: Helpfulness 0.95, Correctness 0.92, F1 0.87, Clarity 0.95, Precision 0.96, media 0.9298)
- [x] Capturar screenshots das avaliacoes. (Evidencias: `evidencias/evidencia_eval_terminal_1.png`, `evidencias/evidencia_eval_terminal_2.png`)
- [x] Capturar ou documentar tracing detalhado de pelo menos 3 exemplos. (Simples, medio e complexo documentados no `README.md` com links publicos gerados pelo Share do LangSmith)

## Entrega Final

- [ ] Confirmar que o repositorio GitHub esta publico.
- [ ] Confirmar que todo codigo-fonte implementado esta no repositorio.
- [x] Confirmar que `prompts/bug_to_user_story_v2.yml` esta completo e funcional.
- [x] Confirmar que `README.md` esta atualizado.
- [x] Confirmar que evidencias do LangSmith estao linkadas ou anexadas.
- [x] Confirmar que os testes passam. (`venv/bin/python -m pytest -q`: 6 passed)
- [x] Confirmar que todas as metricas estao >= 0.8.
- [x] Revisar se nenhum dataset de avaliacao foi alterado.
- [ ] Fazer revisao final antes da submissao.

## Pendencias de informacao

- [x] Obter o link do template mencionado como "Clique aqui para o template": [devfullcycle/mba-ia-pull-evaluation-prompt](https://github.com/devfullcycle/mba-ia-pull-evaluation-prompt).
- [x] Obter o link do repositorio boilerplate do desafio, caso seja diferente do template: [devfullcycle/mba-ia-prompt-engineering](https://github.com/devfullcycle/mba-ia-prompt-engineering).
- [x] Obter o link especifico da documentacao LangSmith indicada no enunciado: <https://docs.smith.langchain.com/>.
- [x] Obter o link especifico do Prompt Engineering Guide indicado no enunciado: <https://www.promptingguide.ai/>.
