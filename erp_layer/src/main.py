from fastapi import FastAPI 
from database import Db

app = FastAPI()

server = 'sql-server-container'
database = 'Demo Database BC (21-0)'
username = 'SA'
password = '/Ferrari499p'
driver = 'ODBC Driver 17 for SQL Server'


connection_string = f'driver={driver};server={server};database={database};uid={username};pwd={password}'

db = Db(connection_string=connection_string)

@app.get("/item")
def get_item():
    return db.get_item()

@app.get("/capacity")
def get_capacity():
    return db.get_capacity()