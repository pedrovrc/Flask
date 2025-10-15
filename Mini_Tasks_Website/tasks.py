from typing import Dict, List, Optional

class TaskStore:
    def __init__(self):
        self._tasks: Dict[int, Dict] = {}
        self._next_id = 1

    def list_tasks(self) -> List[Dict]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Optional[Dict]:
        return self._tasks.get(task_id)

    def create(self, title: str, content: str) -> Dict:
        task = {"id": self._next_id, "title": title, "content": content, "done": False}
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task
    
    def update(self, task_id: int, title: Optional[str] = None, content: Optional[str] = None, done: Optional[bool] = None) -> Optional[Dict]:
        task = self._tasks.get(task_id)
        if not task:
            return None
        if title is not None:
            task["title"] = title
        if content is not None:
            task["content"] = content
        if done is not None:
            task["done"] = bool(done)
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None