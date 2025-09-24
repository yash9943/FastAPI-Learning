from fastapi import FastAPI
from database import engine
from models import Base
from crud import router as crud_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=[""],
#     aloow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"]   
# )

Base.metadata.create_all(bind=engine)

app.include_router(crud_router, prefix="/todo", tags=["Crud Router"])