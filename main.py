from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

class CreateNewAccount(BaseModel):
    user_name : str
    full_name : Annotated[str, Field(min_length=3 ,max_length=50)]
    mail_id : Annotated[str, Field(pattern= r".+@.+\..+")]
    password : str

class Login(BaseModel):
    mail_id : Annotated[str, Field(pattern=r".+@.+\..+")]
    password : str

class CreateTaskReq(BaseModel):
    task_name: str

class UpdateTaskReq(BaseModel):
    id: str
    task_name: str

class DeleteTaskReq(BaseModel):
    id : str
    task_name : str

app = FastAPI()

@app.post("/create_account")
def create_user(create:CreateNewAccount):
    return create

@app.post("/login")
def login_user(login : Login):
    return login

@app.post("/logout")
def logout_user(mail_id : str):
    return login_user.remove(mail_id)

@app.post("/create_task")
def new_task(new_task : CreateTaskReq):
    # db -> save -> id , taskname
    return {
        "task_id": "34567",
        "task_name": new_task.task_name
    }

@app.put("/update_task")
def new_task(new_task : UpdateTaskReq):
    # db -> id , taskname - update -> updated + id
    return {
        "id":"dfdfd", 
        "task_name":new_task.task_name + " learning"
    }

@app.delete("/delete_task")
def delete_task(delete :DeleteTaskReq):
    return {
        "id":"dffff",
        "task_name" : delete.task_name
    }

# value = create_user("ritik","ritik","ritik1008@gmail.com","ruitik")
# print("value : ", value)


from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import Base

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(30))
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

import enum #python enum
class StatusEnum(enum.Enum):
    OPEN = "open"
    COMPLETE = "complete"
    PROGRESS = "progress"

from sqlalchemy import Enum #sqlalchemy enum
class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[StatusEnum] = mapped_column(
        Enum(StatusEnum),
        default=StatusEnum.OPEN
    )

