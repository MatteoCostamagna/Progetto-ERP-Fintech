from fastapi import FastAPI, Query
from database import Db
from model import CapacityLedgerEntry,ItemLedgerEntry
from typing import List
#Creating the object db from class Db, in ./database.py
db = Db("root","/Ferrari499p","fintech-mariadb",3306,"fintech_db")


# Creating the 'item_ledger_entry' and 'capacity_ledger_entry' tables in the database 
db.create_table('item_ledger_entry',ItemLedgerEntry.dict_rep_for_mariadb())
db.create_table('capacity_ledger_entry',CapacityLedgerEntry.dict_rep_for_mariadb())

# Creating a FastAPI instanc
app = FastAPI()

#Endpoint APIs

@app.get("/")
async def root():
    """
    Root endpoint returning a simple message.
    """
    db.connection()
    return {"message": "Hello World"}

@app.post("/upload-item-ledger")
async def upload_item( items_entry : list[ItemLedgerEntry]):
    """
    Endpoint for uploading multiple entries to the 'item_ledger_entry' table.

    Args:
        items_entry (List[ItemLedgerEntry]): List of ItemLedgerEntry objects to be inserted into the database.

    Returns:
        List[ItemLedgerEntry]: List of uploaded ItemLedgerEntry objects.
    """
    db.insert_many_into_table(items_entry, 'item_ledger_entry')
    return items_entry

@app.post("/upload-capacity-ledger")
async def upload_capacity(capacity : list[CapacityLedgerEntry]):
    """
    Endpoint for uploading multiple entries to the 'capacity_ledger_entry' table.

    Args:
        capacity (List[CapacityLedgerEntry]): List of CapacityLedgerEntry objects to be inserted into the database.

    Returns:
        List[CapacityLedgerEntry]: List of uploaded CapacityLedgerEntry objects.
    """
    db.insert_many_into_table(capacity, 'capacity_ledger_entry')
    return capacity

@app.get("/timestamp/{table_name}")
async def get_timestamps(table_name):
    """
    Endpoint for retrieving timestamps from a specified table.

    Args:
        table_name (str): Name of the table from which to retrieve timestamps.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing timestamps.
    """
    return db.get_timestamps(table_name)

@app.delete("/delete/{table_name}/")
async def delete_records(table_name:str,timestamps:List[int] = Query(..., description="List of timestamp for delete")):
    """
    Endpoint for deleting records from a specified table based on timestamps.

    Args:
        table_name (str): Name of the table from which to delete records.
        timestamps (List[int]): List of timestamps for the records to be deleted.

    Returns:
        None: Indicates the success of the operation.
    """
    return db.remove_record(tuple(timestamps),table_name)