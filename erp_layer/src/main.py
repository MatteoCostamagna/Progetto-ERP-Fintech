from fastapi import FastAPI 
from fastapi.encoders import jsonable_encoder
import pyodbc
import datetime
app = FastAPI()

server = 'sql-server-container'
database = 'Demo Database BC (21-0)'
username = 'SA'
password = '/Ferrari499p'
driver = 'ODBC Driver 17 for SQL Server'


connection_string = f'driver={driver};server={server};database={database};uid={username};pwd={password}'

@app.get("/item")
def read_root():
    l = []
    conn = pyodbc.connect(connection_string, autocommit=True)
    cursor = conn.cursor()
    cursor.execute("""SELECT
                    Convert(datetime,[timestamp]),
                    [Entry No_],
                    [Item No_],
                    [Entry Type],
                    [Description],
                    [Location Code],
                    [Quantity],
                    [Remaining Quantity],
                    [Invoiced Quantity],
                    [Transaction Type],
                    [Country_Region Code],
                    [Area],
                    [Order Type],
                    [Completely Invoiced],
                    [Shipped Qty_ Not Returned],
                    [Return Reason Code]
                FROM
                    [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Item Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];
                    """)
    result = cursor.fetchall()
    l = []
    for row in result:
        print(type(row[0]))
        formatted_date = row[0].strftime('%Y-%m-%d %H:%M:%S')
        x = {
            "timestamp": formatted_date.encode('utf-8'),
            "entry_no":row[1],
            "item_no":row[2],
            "entry_type": row[3],
            "description": row[4],
            "location_code": row[5],
            "quantity": row[6],
            "remaining_quantity": row[7],
            "invoiced_quantity": row[8],
            "transaction_type": row[9],
            "country_region_code": row[10],
            "area": row[11],
            "order_type": row[12],
            "completely_invoiced": row[13],
            "shipped_qty_not_returned": row[14],
            "return_reason_code":row[15]
             }
        l.append(x)
    return l
@app.get("/capacity")
def get_capacity():
    l=[]
    conn = pyodbc.connect(connection_string, autocommit=True)
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        CONVERT(time,CONVERT(datetime,[timestamp])),
                        [Entry No_],
                        [Posting Date],
                        [Type],
                        [Description],
                        [Work Center No_],
                        [Quantity],
                        [Setup Time],
                        [Run Time],
                        [Stop Time],
                        [Invoiced Quantity],
                        [Output Quantity],
                        [Scrap Quantity]
                    FROM
                        [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972]
                    ;
""")
    result = cursor.fetchall()
    for row in result:
        x = {
            "timestamp": row[0],
            "entry_no": row[1],
            "posting_date": row[2],
            "type": row[3],
            "Description": row[4],
            "work_center_no_": row[5],
            "quantity": row[6],
            "setup_time": row[7],
            "run_time": row[8],
            "stop_time": row[9],
            "invoiced_quantity": row[10],
            "output_quantity": row[11],
            "scrap_quantity": row[12]
        }
        l.append(x)
    return l


