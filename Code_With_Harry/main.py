# from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

conn = MongoClient()


app = FastAPI()


conn = MongoClient("mongodb://localhost:27017/")




