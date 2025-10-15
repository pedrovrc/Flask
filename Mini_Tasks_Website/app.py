from flask import Flask, render_template, request, redirect, url_for, flash
from tasks import TaskStore

def create_app():
    app = Flask(__name__)
    app.secret_key = "dev-key"  # trocar por algo seguro em produção
    store = TaskStore()

    @app.route("/")
    def index():
        tasks = store.list_tasks()
        return render_template("index.html", tasks=tasks)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title:
                flash("O titulo e obrigatorio", "error")
                return render_template("create.html", title=title, content=content)
            store.create(title, content)
            flash("Tarefa criada com sucesso", "success")
            return redirect(url_for("index"))
        return render_template("create.html")
    
    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit(task_id):
        task = store.get(task_id)
        if not task:
            flash("Tarefa nao encontrada", "error")
            return redirect(url_for("index"))
        if request.method == "POST":
            title = request.form.get("title", "").strip()
            content = request.form.get("content", "").strip()
            if not title:
                flash("O titulo e obrigatorio", "error")
                return render_template("edit.html", task=task)
            store.update(task_id, title=title, content=content)
            flash("Tarefa atualizada com sucesso", "success")
            return redirect(url_for("index"))
        # GET -> mostrar formulário com dados atuais
        return render_template("edit.html", task=task)

    @app.route("/delete/<int:task_id>", methods=["POST"])
    def delete(task_id):
        ok = store.delete(task_id)
        if ok:
            flash("Tarefa removida", "success")
        else:
            flash("Tarefa nao encontrada", "error")
        return redirect(url_for("index"))

    return app