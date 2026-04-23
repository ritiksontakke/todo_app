from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from task import Task, StatusEnum

# ✅ correct import
from repositories import task_repository as task_repo

def create_task(db: Session, task_name: str, due_date: datetime, user_id: int, status: StatusEnum = StatusEnum.OPEN) -> Task:
    task = Task(name=task_name, due_date=due_date, user_id=user_id, status=status)
    return task_repo.create_task(db, task)


def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return task_repo.get_task_by_id(db, task_id)


def get_tasks_by_user(db: Session, user_id: int) -> List[Task]:
    return task_repo.get_tasks_by_user(db, user_id)


def update_task(db: Session, task_id: int, name : str, due_date=None, status=None) -> Optional[Task]:
    print("------step : 2")
    task = task_repo.get_task_by_id(db, task_id)
    print("------step : 4")
    if not task:
        return None

    if name:
        task.name = name
    if due_date:
        task.due_date = due_date
    if status:
        task.status = status

    return task_repo.update_task(db, task)


def delete_task(db: Session, task_id: int) -> bool:
    task = task_repo.get_task_by_id(db, task_id)
    if not task:
        return False

    task_repo.delete_task(db, task)
    return True