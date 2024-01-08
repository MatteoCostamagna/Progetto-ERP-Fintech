from typing import List
from fastapi import FastAPI, Query
from database import Db

# Creazione di un'istanza di FastAPI
app = FastAPI()

# Configurazione delle informazioni di connessione al database
server = 'sql-server-container'
database = 'Demo Database BC (21-0)'
username = 'SA'
password = '/Ferrari499p'
driver = 'ODBC Driver 17 for SQL Server'

# Creazione della stringa di connessione al database
connection_string = f'driver={driver};server={server};database={database};uid={username};pwd={password}'

# Creazione di un'istanza della classe Db con la stringa di connessione
db = Db(connection_string=connection_string)

# Definizione di endpoint per ottenere dati relativi agli item, alla capacità e ai timestamp
@app.get("/item")
async def get_item():
    """
    Endpoint per ottenere dati dalla tabella '$Item Ledger Entry$' del database.
    """
    return db.get_item()

@app.get("/capacity")
async def get_capacity():
    """
    Endpoint per ottenere dati dalla tabella '$Capacity Ledger Entry$' del database.
    """
    return db.get_capacity()

@app.get("/timestamp/capacity")
async def get_timestamps_capacity():
    """
    Endpoint per ottenere i timestamp dalla tabella '$Capacity Ledger Entry$' del database.
    """
    return db.get_timestamps_capacity()

@app.get("/timestamp/item")
async def get_timestamps_item():
    """
    Endpoint per ottenere i timestamp dalla tabella '$Item Ledger Entry$' del database.
    """
    return db.get_timestamps_item()

@app.get("/item/")
async def get_item_by_ts(timestamps: List[int] = Query(..., description="List of timestamps")):
    """
    Endpoint per ottenere dati dalla tabella '$Item Ledger Entry$' del database per timestamp specifici.
    Args:
        timestamps (List[int]): Lista di timestamp per cui recuperare i dati.
    """
    return db.get_item_by_ts(tuple(timestamps))

@app.get("/capacity/")
async def get_capacity_by_ts(timestamps: List[int] = Query(..., description="List of timestamps")):
    """
    Endpoint per ottenere dati dalla tabella '$Capacity Ledger Entry$' del database per timestamp specifici.
    Args:
        timestamps (List[int]): Lista di timestamp per cui recuperare i dati.
    """
    return db.get_capacity_by_ts(tuple(timestamps))