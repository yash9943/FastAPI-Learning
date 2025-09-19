from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id : int
    name : str
    origin : str
    
teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_teas(tea_id: int, updated_tea: Tea):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[i] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_teas(tea_id: int):
    for i, tea in enumerate(teas):
        if tea.id == tea_id:
            teas.pop(i)
            return {"message": "Tea deleted"}
    return {"error": "Tea not found"}