from sqlalchemy.orm import Session
from typing import List, Optional
from user import User


def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()


def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    db.commit()