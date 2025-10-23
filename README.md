# Projetos de estudo — Flask (mini-projetos)

Este repositório contém três mini-projetos para aprender Flask, cada um em sua própria pasta:

- `Mini_Task_API/` — Mini API de Tarefas (To-Do) — servidor REST simples com armazenamento em memória e testes.
- `Mini_Tasks_Website/` — Site simples de lista tarefas com formulários e templates HTML (Jinja).
- `Database_and_API/` — Projeto completo com banco de dados SQLAlchemy, Flask-Migrate, API RESTful e interface web.

---

Este README explica como rodar e testar os subprojetos dentro desse repositório.

---

## Mini_Task_API — visão geral

Estrutura mínima dentro de `Mini_Task_API`:

- `app.py` — factory `create_app()` e rotas REST (GET/POST/PUT/DELETE) para `/tasks`.
- `tasks.py` — `TaskStore` em memória (CRUD básico).
- `tests/` — testes automatizados com `pytest` que usam `app.test_client()`.
- `requirements.txt` — dependências do projeto (Flask, pytest).

O servidor foi mantido propositalmente simples para fins didáticos.

## Como rodar localmente (Windows / PowerShell)

1. Abra o PowerShell na raiz do repositório.

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

## Mini_Tasks_Website — visão geral

Estrutura mínima dentro de `Mini_Tasks_Website`:

- `app.py` — factory `create_app()` e rotas para páginas (index, create, edit, delete).
- `tasks.py` — `TaskStore` em memória com métodos create/get/list/update/delete.
- `templates/` — `base.html`, `index.html`, `create.html`, `edit.html` (Jinja2 templates).
- `static/` — CSS e recursos estáticos.
- `tests/` — testes com `pytest` simulando requisições via `app.test_client()`.

### Como rodar localmente (Windows / Powershell)

1. Abra o PowerShell na pasta do subprojeto (Mini_Tasks_Website)

2. Ative o ambiente virtual criado na raiz do repo (ou crie/ative um aqui):

```powershell
.venv\Scripts\Activate.ps1
```

3. Instale dependências:

```powershell
pip install -r requirements.txt
```

4. Rodar a aplicação:

```powershell
$env:FLASK_APP="app:create_app"
flask run
```

Abra o navegador em `http://127.0.0.1:5000`.

### Testes (Mini_Tasks_Website)

Se você adicionou a pasta `tests/` dentro do subprojeto, rode os testes assim (na pasta `Mini_Tasks_Website`):

```powershell
python -m pytest -q
```

---

## Database_and_API — visão geral

Projeto Flask com arquitetura em camadas, banco de dados SQLAlchemy, Flask-Migrate, API RESTful e interface web.

**Principais arquivos e estrutura:**
- `app.py`: Factory da aplicação Flask, registro dos blueprints e inicialização do banco/migrações
- `models.py`: Modelos SQLAlchemy (Task)
- `repositories.py`: Camada de acesso a dados (CRUD)
- `services.py`: Regras de negócio e validação
- `api.py`: Blueprint da API RESTful (`/api/v1/tasks`)
- `web.py`: Blueprint da interface web (páginas HTML)
- `config.py`: Configurações (SECRET_KEY, URI do banco)
- `requirements.txt`: Dependências
- `migrations/`: Migrações do banco (Alembic)
- `templates/`: Templates HTML (Jinja2)
- `tests/`: Testes automatizados com banco em memória

### Como rodar localmente (Windows / PowerShell)

1. Abra o PowerShell na pasta `Database_and_API`.

2. Crie e ative um ambiente virtual (recomendado):
	```powershell
	python -m venv .venv
	.venv\Scripts\Activate.ps1
	```
3. Instale as dependências:
	```powershell
	pip install -r requirements.txt
	```
4. Inicialize as migrações e o banco:
	```powershell
	flask db init
	flask db migrate
	flask db upgrade
	```
5. Rode a aplicação:
	```powershell
	python app.py
	```

### Testes

Execute os testes automatizados:
```powershell
pytest
```

### Endpoints principais

- API: `/api/v1/tasks` (GET, POST, PUT, DELETE)
- Web: `/` (listar, criar, editar, deletar tarefas)

### Observações
- Banco padrão: SQLite (`tasks.db`)
- Para testes, usa SQLite em memória
- Regras de negócio e validação no `services.py`
- Transações e erros tratados no repositório

## Próximos passos e ideias de evolução

- ✅ Concluir API simples de tarefas - Praticar aplicação básica de servidor REST simples com Flask.
- ✅ Concluir Site de tarefas - Praticar uso de templates HTML (Jinja2) e formulários.
- ✅ Concluir Banco de Dados + API - Integração das partes anteriores com um banco de dados persistente.

---
