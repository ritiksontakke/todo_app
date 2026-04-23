from sqlalchemy.orm import Session
from typing import List, Optional
from task import Task, StatusEnum


def create_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    print("------step : 3")
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks_by_user(db: Session, user_id: int) -> List[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()


def update_task(db: Session, task: Task) -> Task:
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()