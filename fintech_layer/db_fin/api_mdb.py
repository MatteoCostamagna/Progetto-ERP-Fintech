from fastapi import FastAPI
from database import Db
from model import CapacityLedgerEntry,ItemLedgerEntry
#Creating the object db from class Db, in ./database.py
db = Db("root","/Ferrari499p","fintech-mariadb",3306,"fintech_db")

#Creating the tables in the db
 
db.create_table('item_ledger_entry',ItemLedgerEntry.dict_rep_for_mariadb())
db.create_table('capacity_ledger_entry',CapacityLedgerEntry.dict_rep_for_mariadb())

app = FastAPI()

@app.get("/")
async def root():
    db.connection()
    return {"message": "Hello World"}

@app.post("/upload-item-ledger")
async def upload_item( items_entry : list[ItemLedgerEntry]):
    db.insert_many_into_table(items_entry, 'item_ledger_entry')
    return items_entry

@app.post("/upload-capacity-ledger")
async def upload_capacity(capacity : list[CapacityLedgerEntry]):
    db.insert_many_into_table(capacity, 'capacity_ledger_entry')
    return capacity

@app.get("/timestamp/{table_name}")
async def get_timestamps(table_name):
    return db.get_timestamps(table_name)