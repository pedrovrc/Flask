# Projetos de estudo — Flask (mini-projetos)

Este repositório contém três mini-projetos para aprender Flask, cada um em sua própria pasta:

- `Mini_Task_API/` — Mini API de Tarefas (To-Do) — servidor REST simples com armazenamento em memória e testes.
- `Mini_Notes_Website/` — (placeholder) site de notas — projeto a ser implementado.
- `Database_and_API/` — (placeholder) exemplos de banco de dados e API — projeto a ser implementado.

Este README explica como rodar e testar o `Mini_Task_API`, que é o projeto inicial implementado.

---

## Mini_Task_API — visão geral

Estrutura mínima dentro de `Mini_Task_API`:

- `app.py` — factory `create_app()` e rotas REST (GET/POST/PUT/DELETE) para `/tasks`.
- `tasks.py` — `TaskStore` em memória (CRUD básico).
- `tests/` — testes automatizados com `pytest` que usam `app.test_client()`.
- `requirements.txt` — dependências do projeto (Flask, pytest).

O servidor foi mantido propositalmente simples para fins didáticos.

## Como rodar localmente (Windows / PowerShell)

1. Abra o PowerShell na raiz do repositório (`F:\Programming\Flask`).

2. Crie e ative um ambiente virtual (recomendado):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Instale dependências (dentro de `Mini_Task_API`):

```powershell
cd Mini_Task_API
pip install -r requirements.txt
```

4. Rodar a aplicação (a partir de `Mini_Task_API`):

```powershell
# Defina a variável de ambiente para a factory (opcional)
#$env:FLASK_APP="app:create_app"
#$env:FLASK_ENV="development"
flask run
```

Ou, sem usar `flask run` (mais explícito):

```powershell
python -c "from app import create_app; create_app().run(debug=True)"
```

O servidor ficará disponível em `http://127.0.0.1:5000`.

5. Testes automatizados (a partir de `Mini_Task_API`):

```powershell
# com o venv ativado
python -m pytest -q
```

---

## Endpoints principais (exemplos)

- GET /tasks — lista todas as tarefas
- GET /tasks/<id> — pega tarefa por id
- POST /tasks — cria tarefa (payload JSON: {"title": "texto"})
- PUT /tasks/<id> — atualiza tarefa (p.ex. {"done": true})
- DELETE /tasks/<id> — remove tarefa

Exemplo usando PowerShell (Invoke-RestMethod):

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/tasks -Body (ConvertTo-Json @{ title = 'Comprar leite' }) -ContentType 'application/json'
Invoke-RestMethod http://127.0.0.1:5000/tasks
```

---

## Próximos passos e ideias de evolução

- Concluir Site de notas - Praticar uso de templates HTML (Jinja2) e formulários.
- Concluir Banco de Dados + API - Integração das partes anteriores.

---
