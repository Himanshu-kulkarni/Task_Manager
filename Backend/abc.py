from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class User(BaseModel):
    name: str

@app.get("/home")
def home_page():
    return {"message": "this is home page"}

@app.get("/hello")
def hello():
    return {"msg": "hello"}

@app.post("/tasks")
def create_task(user: User):
    tasks.append(user.name)
    return {"message": "task added", "tasks": tasks}