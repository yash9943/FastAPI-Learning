from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/hello")
async def hello():
    return {"message":"Hello, How are you ?"}

@app.get("/item/{Item}")
def path_func(Item):
    var_name = {"Path variable":Item}
    return var_name

@app.get("/query")
def query_func(name: str, roll_no: int):
    var_name = {"Name":name, "roll no":roll_no}
    return var_name