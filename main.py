from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

def create_user(user_name,full_name,mail_id,password):
    # print("user_name : " , user_name)
    # print("full_name : ", full_name)
    # print("mail_id : ", mail_id)

    return {
        "user_name" : user_name,
        "full_name" : full_name,
        "mail_id" : mail_id,
        "password" : password
    }

# value = create_user("ritik","ritik","ritik1008@gmail.com","ruitik")
# print("value : ", value)



















