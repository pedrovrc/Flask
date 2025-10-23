"""
api.py: API blueprint for RESTful task operations.
"""
from flask import Blueprint, request, jsonify
from services import TaskService
from sqlalchemy.exc import IntegrityError

api_bp = Blueprint('api', __name__, url_prefix='/api/v1/tasks')

@api_bp.route('/', methods=['GET'])
def list_tasks():
    tasks = TaskService.list_tasks()
    return jsonify([{'id': t.id, 'title': t.title, 'done': t.done} for t in tasks])

@api_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = TaskService.get_task(task_id)
    if not task:
        return jsonify({'error': 'Tarefa não encontrada.'}), 404
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done})

@api_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title', '')
    task, error = TaskService.create_task(title)
    if error:
        return jsonify({'error': error}), 400
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done}), 201

@api_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    title = data.get('title')
    done = data.get('done')
    task, error = TaskService.update_task(task_id, title, done)
    if error:
        if error == "Tarefa não encontrada.":
            return jsonify({'error': error}), 404
        return jsonify({'error': error}), 400
    return jsonify({'id': task.id, 'title': task.title, 'done': task.done})

@api_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    success, error = TaskService.delete_task(task_id)
    if error:
        if error == "Tarefa não encontrada.":
            return jsonify({'error': error}), 404
        return jsonify({'error': error}), 400
    return jsonify({'result': 'ok'})