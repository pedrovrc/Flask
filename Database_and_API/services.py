"""
services.py: Business logic layer for Task operations.
"""
from repositories import TaskRepository

MAX_TITLE_LENGTH = 128

class TaskService:
    @staticmethod
    def validate_title(title):
        if not title or not title.strip():
            return False, "Título não pode ser vazio."
        if len(title.strip()) > MAX_TITLE_LENGTH:
            return False, f"Título deve ter no máximo {MAX_TITLE_LENGTH} caracteres."
        return True, ""

    @staticmethod
    def create_task(title):
        valid, msg = TaskService.validate_title(title)
        if not valid:
            return None, msg
        title = title.strip()
        try:
            task = TaskRepository.create(title)
            return task, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def update_task(task_id, title=None, done=None):
        if title is not None:
            valid, msg = TaskService.validate_title(title)
            if not valid:
                return None, msg
            title = title.strip()
        try:
            task = TaskRepository.update(task_id, title, done)
            if not task:
                return None, "Tarefa não encontrada."
            return task, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def delete_task(task_id):
        try:
            result = TaskRepository.delete(task_id)
            if not result:
                return False, "Tarefa não encontrada."
            return True, None
        except Exception as e:
            return False, str(e)

    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_by_id(task_id)

    @staticmethod
    def list_tasks():
        return TaskRepository.get_all()