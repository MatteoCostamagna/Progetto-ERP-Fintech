from pydantic import BaseModel
from datetime import datetime


class ItemLedgerEntry(BaseModel):
    timestamp: int
    entry_no: int
    item_no: str
    entry_type: int
    description: str
    location_code: str
    quantity:float
    remaining_quantity: float
    invoiced_quantity: float
    transaction_type: str
    country_region_code: str
    area: str
    order_type: int
    completely_invoiced: int
    shipped_qty_not_returned: float
    return_reason_code: str

    @staticmethod
    def dict_rep_for_mariadb():
        return {
            "timestamp": "BIGINT",
            "entry_no": "INT",
            "item_no" : "VARCHAR(4)",
            "entry_type": "TINYINT",
            "description": "TEXT",
            "location_code":"TEXT",
            "quantity": "DECIMAL(38, 0)",
            "remaining_quantity": "DECIMAL(38, 0)",
            "invoiced_quantity": "DECIMAL(38, 0)",
            "transaction_type": "TEXT",
            "country_region_code": "TEXT",
            "area": "TEXT",
            "order_type": "TINYINT",
            "completely_invoiced": "TINYINT",
            "shipped_qty_not_returned": "DECIMAL(38, 0)",
            "return_reason_code": "TEXT"
        }
    
class CapacityLedgerEntry(BaseModel):
    timestamp: int
    Entry_No: int
    Posting_Date: datetime
    Type: int
    Description: str
    Work_Center_No: str
    Quantity: float
    Setup_Time: float
    Run_Time: float
    Stop_Time: float
    Invoiced_Quantity: float
    Output_Quantity: float
    Scrap_Quantity: float

    @staticmethod
    def dict_rep_for_mariadb():
        return {
            "timestamp": "BIGINT",
            "entry_no": "INT",
            "posting_date": "DATETIME",
            "type": "INT",
            "description": "TEXT",
            "work_center_no_": "VARCHAR(255)",
            "quantity": "DECIMAL(38, 0)",
            "setup_time": "DECIMAL(38, 0)",
            "run_time": "DECIMAL(38, 0)",
            "stop_time": "DECIMAL(38, 0)",
            "invoiced_quantity": "DECIMAL(38, 0)",
            "output_quantity": "DECIMAL(38, 0)",
            "scrap_quantity": "DECIMAL(38, 0)"
        }