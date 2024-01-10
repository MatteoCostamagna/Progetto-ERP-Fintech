from typing import List
from fastapi import FastAPI, Query
from database import Db

# Creating an instance of FastAPI
app = FastAPI()

# Configuring database connection information
server = 'sql-server-container'
database = 'Demo Database BC (21-0)'
username = 'SA'
password = '/Ferrari499p'
driver = 'ODBC Driver 17 for SQL Server'

# Creating the database connection string
connection_string = f'driver={driver};server={server};database={database};uid={username};pwd={password}'

# Creating an instance of the Db class with the connection string
db = Db(connection_string=connection_string)

# Defining endpoints to retrieve data related to items, capacity, and timestamps
@app.get("/item")
async def get_item():
    """
    Endpoint to retrieve data from the '$Item Ledger Entry$' table of the database.
    """
    return db.get_item()

@app.get("/capacity")
async def get_capacity():
    """
    Endpoint to retrieve data from the '$Capacity Ledger Entry$' table of the database.
    """
    return db.get_capacity()

@app.get("/timestamp/capacity")
async def get_timestamps_capacity():
    """
    Endpoint to retrieve timestamps from the '$Capacity Ledger Entry$' table of the database.
    """
    return db.get_timestamps_capacity()

@app.get("/timestamp/item")
async def get_timestamps_item():
    """
    Endpoint to retrieve timestamps from the '$Item Ledger Entry$' table of the database.
    """
    return db.get_timestamps_item()

@app.get("/item/")
async def get_item_by_ts(timestamps: List[int] = Query(..., description="List of timestamps")):
    """
    Endpoint to retrieve data from the '$Item Ledger Entry$' table of the database for specific timestamps.
    Args:
        timestamps (List[int]): List of timestamps for which to retrieve the data.
    """
    return db.get_item_by_ts(tuple(timestamps))

@app.get("/capacity/")
async def get_capacity_by_ts(timestamps: List[int] = Query(..., description="List of timestamps")):
    """
    Endpoint to retrieve data from the '$Capacity Ledger Entry$' table of the database for specific timestamps.
    Args:
        timestamps (List[int]): List of timestamps for which to retrieve the data.
    """
    return db.get_capacity_by_ts(tuple(timestamps))