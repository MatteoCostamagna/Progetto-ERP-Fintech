from typing import List
from fastapi import FastAPI, Query
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
async def get_item():
    return db.get_item()

@app.get("/capacity")
async def get_capacity():
    return db.get_capacity()

@app.get("/timestamp/capacity")
async def get_timestamps_capacity():
    return db.get_timestamps_capacity()

@app.get("/timestamp/item")
async def get_timestamps_item():
    return db.get_timestamps_item()

@app.get("/item/")
async def get_item_by_ts(timestamps: List[int] = Query(..., description="List of timestamps")):
    return db.get_item_by_ts(tuple(timestamps))

@app.get("/capacity/")
async def get_capacity_by_ts(timestamps: List[int] = Query(..., description="List of timestamps")):
    return db.get_capacity_by_ts(tuple(timestamps))