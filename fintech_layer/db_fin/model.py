from pydantic import BaseModel
from datetime import datetime


class ItemLedgerEntry(BaseModel):
    """
    Pydantic model representing an entry in the 'Item Ledger Entry' table.

    Attributes:
        timestamp (int): Timestamp of the entry.
        entry_no (int): Entry number.
        item_no (str): Item number.
        posting_date (datetime): Posting date of the entry.
        entry_type (int): Entry type.
        description (str): Description of the entry.
        location_code (str): Location code.
        quantity (float): Quantity.
        remaining_quantity (float): Remaining quantity.
        invoiced_quantity (float): Invoiced quantity.
        transaction_type (str): Transaction type.
        country_region_code (str): Country/Region code.
        area (str): Area.
        order_type (int): Order type.
        completely_invoiced (int): Indicator for completely invoiced.
        shipped_qty_not_returned (float): Shipped quantity not returned.
        return_reason_code (str): Return reason code.

    Methods:
        dict_rep_for_mariadb(): Returns a dictionary representing the data types for MariaDB.
    """
    timestamp: int
    entry_no: int
    item_no: str
    posting_date: datetime
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
            "item_no" : "VARCHAR(25)",
            "posting_date": "DATETIME",
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
    """
    Pydantic model representing an entry in the 'Capacity Ledger Entry' table.

    Attributes:
        timestamp (int): Timestamp of the entry.
        entry_no (int): Entry number.
        posting_date (datetime): Posting date of the entry.
        type (int): Type of the entry.
        description (str): Description of the entry.
        work_center_no (str): Work center number.
        quantity (float): Quantity.
        setup_time (float): Setup time.
        run_time (float): Run time.
        stop_time (float): Stop time.
        invoiced_quantity (float): Invoiced quantity.
        output_quantity (float): Output quantity.
        scrap_quantity (float): Scrap quantity.

    Methods:
        dict_rep_for_mariadb(): Returns a dictionary representing the data types for MariaDB.
    """
    timestamp: int
    entry_no: int
    posting_date: datetime
    type: int
    description: str
    work_center_no: str
    quantity: int
    setup_time: int
    run_time: int
    stop_time: int
    invoiced_quantity: int
    output_quantity: int
    scrap_quantity: int
    operation_no: int

    @staticmethod
    def dict_rep_for_mariadb():
        return {
            "timestamp": "BIGINT",
            "entry_no": "INT",
            "posting_date": "DATETIME",
            "type": "INT",
            "description": "TEXT",
            "work_center_no": "VARCHAR(255)",
            "quantity": "DECIMAL(38, 0)",
            "setup_time": "DECIMAL(38, 0)",
            "run_time": "DECIMAL(38, 0)",
            "stop_time": "DECIMAL(38, 0)",
            "invoiced_quantity": "DECIMAL(38, 0)",
            "output_quantity": "DECIMAL(38, 0)",
            "scrap_quantity": "DECIMAL(38, 0)",
            "operation_no": "INTEGER"
        }