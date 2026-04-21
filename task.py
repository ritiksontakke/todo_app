from typing import Optional
from sqlalchemy import String , DateTime,Enum , ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped , relationship
from sqlalchemy.orm import mapped_column
from db import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

import enum #python enum
class StatusEnum(enum.Enum):
    OPEN = "open"
    COMPLETE = "complete"
    PROGRESS = "progress"

from sqlalchemy import Enum #sqlalchemy enum
class Task(Base):
    __tablename__ = "Task"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum),
        default=StatusEnum.OPEN
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    due_date : Mapped[datetime] = mapped_column(
        DateTime
    )

    updated_at : Mapped[datetime] = mapped_column(
        DateTime,
        default = datetime.utcnow,
        onupdate=datetime.utcnow
    )
    
    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    user : Mapped["User"] = relationship(back_populates="tasks")


