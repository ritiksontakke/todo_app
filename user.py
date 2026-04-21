from __future__ import annotations
from typing import Optional,List,TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped ,relationship
from sqlalchemy.orm import mapped_column

from db import Base

if TYPE_CHECKING:
    from .task import Task

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    full_name: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(30))
    # task : Mapped[List["Task"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
