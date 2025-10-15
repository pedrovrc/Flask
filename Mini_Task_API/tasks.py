from typing import Dict, List, Optional

class TaskStore:
    def __init__(self):
        self._tasks: Dict[int, Dict] = {}
        self._next_id = 1

    def list_tasks(self) -> List[Dict]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Optional[Dict]:
        return self._tasks.get(task_id)

    def create(self, data: Dict) -> Dict:
        task = {"id": self._next_id, "title": data.get("title", ""), "done": bool(data.get("done", False))}
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def update(self, task_id: int, data: Dict) -> Optional[Dict]:
        task = self._tasks.get(task_id)
        if not task:
            return None # 404
        task["title"] = data.get("title", task["title"])
        task["done"] = bool(data.get("done", task["done"]))
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None