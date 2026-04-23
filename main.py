from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from sqlalchemy.orm import Session
from db import get_db, engine, Base
from datetime import datetime
from services import user_service , task_service
from fastapi import Depends
import user
import task

class CreateNewAccount(BaseModel):
    full_name : Annotated[str, Field(min_length=3 ,max_length=50)]
    email : Annotated[str, Field(pattern= r".+@.+\..+")]
    password : str

class Login(BaseModel):
    email  : Annotated[str, Field(pattern=r".+@.+\..+")]
    password : str

class CreateTaskReq(BaseModel):
    task_name: str
    due_date: datetime
    user_id : int
    status : str
    

class UpdateTaskReq(BaseModel):
    id: str
    task_name: str

class DeleteTaskReq(BaseModel):
    id : str
    task_name : str

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("Non exisiting table were crated sucessfully")

@app.post("/create_account")
def create_user(create:CreateNewAccount, db: Session = Depends(get_db)):
    return user_service.create_user(db, create.email, create.password, create.full_name)

@app.post("/login")
def login_user(login : Login, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, login.email, login.password)

@app.post("/logout")
def logout_user(mail_id : str):
    return "logout"

@app.post("/create_task")
def create_task(new_task : CreateTaskReq, db: Session = Depends(get_db)):    
    return task_service.create_task(db, new_task.task_name, new_task.due_date, new_task.user_id, new_task.status)

@app.put("/update_task_abc")
def update_task(update_task : UpdateTaskReq, db: Session = Depends(get_db)):
    print("------step : 1")
    res = task_service.update_task(db=db, task_id=update_task.id, name=update_task.task_name)
    print("------step : 5")
    return res


@app.delete("/delete_task")
def delete_task(delete: DeleteTaskReq, db: Session = Depends(get_db)):
    return {
        "id":"dffff",
        "task_name" : delete.task_name
    }

# value = create_user("ritik","ritik","ritik1008@gmail.com","ruitik")
# print("value : ", value)
