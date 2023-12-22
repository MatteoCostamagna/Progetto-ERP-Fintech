from fastapi import FastAPI
from database import Db

#Creating the object db from class Db, in ./database.py
db = Db("root","/Ferrari499p","fintech-mariadb",3306,"fintech_db")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}