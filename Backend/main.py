from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = []

class User(BaseModel):
    name: str

@app.get("/home")
def home_page():
    return {"message": "this is home page"}

@app.get("/hello")
def hello():
    return {"msg": "hello"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(user: User):
    tasks.append(user.name)
    return {"message": "task added", "tasks": tasks}