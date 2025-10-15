from flask import Flask, jsonify, request, abort
from tasks import TaskStore

def create_app():
    app = Flask(__name__)
    store = TaskStore()

    @app.route("/tasks", methods=["GET"])
    def list_tasks():
        return jsonify(store.list_tasks())

    @app.route("/tasks/<int:task_id>", methods=["GET"])
    def get_task(task_id):
        task = store.get(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(task)

    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json(force=True)
        title = data.get("title") if isinstance(data, dict) else None
        if not title:
            return jsonify({"error": "Missing 'title'"}), 400
        task = store.create({"title": title, "done": False})
        return jsonify(task), 201

    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        data = request.get_json(force=True)
        task = store.get(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404
        title = data.get("title", task["title"])
        done = data.get("done", task["done"])
        updated = store.update(task_id, {"title": title, "done": bool(done)})
        return jsonify(updated)

    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        ok = store.delete(task_id)
        if not ok:
            return jsonify({"error": "Task not found"}), 404
        return "", 204

    return app