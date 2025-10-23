"""
repositories.py: Data access layer for Task model using SQLAlchemy.
"""
from models import db, Task
from sqlalchemy.exc import IntegrityError

class TaskRepository:
    @staticmethod
    def get_all():
        return Task.query.order_by(Task.created_at.desc()).all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def create(title):
        task = Task(title=title)
        db.session.add(task)
        try:
            db.session.commit()
            return task
        except IntegrityError:
            db.session.rollback()
            raise

    @staticmethod
    def update(task_id, title=None, done=None):
        task = Task.query.get(task_id)
        if not task:
            return None
        if title is not None:
            task.title = title
        if done is not None:
            task.done = done
        try:
            db.session.commit()
            return task
        except IntegrityError:
            db.session.rollback()
            raise

    @staticmethod
    def delete(task_id):
        task = Task.query.get(task_id)
        if not task:
            return None
        db.session.delete(task)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            raise