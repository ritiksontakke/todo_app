from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from user import User
from task import Task, StatusEnum


# ------------------------
# USER SERVICES
# ------------------------

def create_user(db: Session, email_name: str, password: str, fullname: Optional[str] = None) -> User:
    user = User(
        email_name=email_name,
        password=password,
        fullname=fullname
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()


def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True


# ------------------------
# TASK SERVICES
# ------------------------

def create_task(
    db: Session,
    name: str,
    due_date: datetime,
    user_id: int,
    status: StatusEnum = StatusEnum.OPEN
) -> Task:
    task = Task(
        name=name,
        due_date=due_date,
        user_id=user_id,
        status=status
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks_by_user(db: Session, user_id: int) -> List[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()


def update_task_status(db: Session, task_id: int, status: StatusEnum) -> Optional[Task]:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    task.status = status
    db.commit()
    db.refresh(task)
    return task


def update_task(
    db: Session,
    task_id: int,
    name: Optional[str] = None,
    due_date: Optional[datetime] = None,
    status: Optional[StatusEnum] = None
) -> Optional[Task]:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    if name:
        task.name = name
    if due_date:
        task.due_date = due_date
    if status:
        task.status = status

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True