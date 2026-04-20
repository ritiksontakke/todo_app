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
