from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id : int
    name : str
    description : str
    
todos = []

@app.get("/")
def show_todo():
    return todos

@app.post('/')
def create_todo(todo: ToDo):
    todos.append(todo)
    return {"message":"ToDo added succesfully"}

@app.put('/')
def home():
    return {"message":"This is put request"}