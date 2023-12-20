from fastapi import FastAPI
from database import Db

db = Db("root","/Ferrari499p","")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}