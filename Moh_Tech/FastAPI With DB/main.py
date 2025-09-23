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

@app.put('/{todo_id}')
def updated_todo(todo_id: int, updated_todo: ToDo):
    for i,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message":"Your todo has been updated"}
        else:
            return {"message":"Faild to update todo"}
            
            
@app.delete("/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message":"Your todo is deleted"}