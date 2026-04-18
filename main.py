from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated


class CreateNewAccount(BaseModel):
    user_name : str
    full_name : Annotated[str, Field(min_length=3 ,max_length=50)]
    mail_id : Annotated[str, Field(pattern= r".+@.+\..+")]
    password : str


app = FastAPI()


@app.post("/create_account/")
def create_user(creat:CreateNewAccount ):
    return creat


# value = create_user("ritik","ritik","ritik1008@gmail.com","ruitik")
# print("value : ", value)


















