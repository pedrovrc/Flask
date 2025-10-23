"""
web.py: Web blueprint for task management pages.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services import TaskService

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    tasks = TaskService.list_tasks()
    return render_template('index.html', tasks=tasks)

@web_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title', '')
        task, error = TaskService.create_task(title)
        if error:
            flash(error, 'danger')
            return render_template('create.html')
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('web.index'))
    return render_template('create.html')

@web_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = TaskService.get_task(task_id)
    if not task:
        flash('Tarefa não encontrada.', 'danger')
        return redirect(url_for('web.index'))
    if request.method == 'POST':
        title = request.form.get('title')
        done = request.form.get('done') == 'on'
        updated_task, error = TaskService.update_task(task_id, title, done)
        if error:
            flash(error, 'danger')
            return render_template('edit.html', task=task)
        flash('Tarefa atualizada!', 'success')
        return redirect(url_for('web.index'))
    return render_template('edit.html', task=task)

@web_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    success, error = TaskService.delete_task(task_id)
    if error:
        flash(error, 'danger')
    elif success:
        flash('Tarefa deletada!', 'success')
    return redirect(url_for('web.index'))