from sqlalchemy.orm import Session
from typing import List, Optional
from user import User
from repositories import user_repository as user_repo


def create_user(db: Session, email: str, password: str, full_name: Optional[str] = None) -> User:
    user = User(email=email, password=password, full_name=full_name)
    return user_repo.create_user(db, user)


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return user_repo.get_user_by_id(db, user_id)


def get_all_users(db: Session) -> List[User]:
    return user_repo.get_all_users(db)


def delete_user(db: Session, user_id: int) -> bool:
    user = user_repo.get_user_by_id(db, user_id)
    if not user:
        return False
    user_repo.delete_user(db, user)
    return True