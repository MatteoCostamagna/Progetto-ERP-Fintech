import pyodbc

class Db:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def connection(self):
        
        conn = None
        
        try:
            
            conn = pyodbc.connect(self.connection_string, autocommit=True)
        
        except pyodbc.Error as e:
            
            print(e)
        
        return conn

    def get_capacity(self):
        
        l = []
        
        conn = self.connection()
        
        cursor = conn.cursor()
        
        cursor.execute("""
                    SELECT
                        CONVERT(bigint,[timestamp]),
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
                "description": row[4],
                "work_center_no_": row[5],
                "quantity": float(row[6]),
                "setup_time": float(row[7]),
                "run_time": float(row[8]),
                "stop_time": float(row[9]),
                "invoiced_quantity": float(row[10]),
                "output_quantity": float(row[11]),
                "scrap_quantity": float(row[12])
                }
        
            l.append(x)
    
        return l
    
    def get_item(self):
        
        l = []
        
        conn = self.connection()
        
        cursor = conn.cursor()

        cursor.execute("""
                SELECT
                    Convert(bigint,[timestamp]),
                    [Entry No_],
                    [Item No_],
                    [Posting Date],
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
    
        for row in result:
            
            x = {
                "timestamp": row[0],
                "entry_no":row[1],
                "item_no":row[2],
                "posting_date":row[3],
                "entry_type": row[4],
                "description": row[5],
                "location_code": row[6],
                "quantity": row[7],
                "remaining_quantity": row[8],
                "invoiced_quantity": row[9],
                "transaction_type": row[10],
                "country_region_code": row[11],
                "area": row[12],
                "order_type": row[13],
                "completely_invoiced": row[14],
                "shipped_qty_not_returned": row[15],
                "return_reason_code":row[16]
                }
            l.append(x)
        
        return l
    
    def get_timestamps_capacity(self):
        
        conn = self.connection()

        cursor = conn.cursor()

        query = f"SELECT convert(bigint,[timestamp]) FROM [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];"

        l = []
        
        try:
            
            cursor.execute(query)
            
            for row in cursor:
                
                x = {"timestamp":row[0]}
                
                l.append(x)
            
            return l
        
        except pyodbc.Error as e:
        
            print(f'Error:{e}')
            return {'Error': e}
            
    def get_timestamps_item(self):
        
        conn = self.connection()

        cursor = conn.cursor()

        query = f"SELECT convert(bigint,[timestamp]) FROM [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Item Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];"

        l = []
        
        try:
            
            cursor.execute(query)
            
            for row in cursor:
                
                x = {"timestamp":row[0]}
                
                l.append(x)
            
            return l
        
        except pyodbc.Error as e:
        
            print(f'Error:{e}')
            return {'Error': e}
        
    def get_capacity_by_ts(self, ts_to_get):
        
        l = []
        
        conn = self.connection()
        
        cursor = conn.cursor()

        query =f"""
               SELECT
                        CONVERT(bigint,[timestamp]),
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
                WHERE 
                    convert(bigint,[timestamp]) IN  ({', '.join(["?" for _ in ts_to_get])})
                       ;
                    """
        try:
            cursor.execute(query,ts_to_get)
            result = cursor.fetchall()
        
            for row in result:
                
                x = {
                    "timestamp": row[0],
                    "entry_no": row[1],
                    "posting_date": row[2],
                    "type": row[3],
                    "description": row[4],
                    "work_center_no_": row[5],
                    "quantity": float(row[6]),
                    "setup_time": float(row[7]),
                    "run_time": float(row[8]),
                    "stop_time": float(row[9]),
                    "invoiced_quantity": float(row[10]),
                    "output_quantity": float(row[11]),
                    "scrap_quantity": float(row[12])
                    }
                l.append(x)
            
            return l
        except pyodbc.Error as e:
        
            print(f'Error:{e}')
            return {'Error': e}

    
    def get_item_by_ts(self,ts_to_get:tuple):

        l = []
        
        conn = self.connection()
        
        cursor = conn.cursor()

        query =f"""SELECT
                    Convert(bigint,[timestamp]),
                    [Entry No_],
                    [Item No_],
                    [Posting Date],
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
                    [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Item Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972]
                WHERE
                    convert(bigint,[timestamp]) IN  ({', '.join(["?" for _ in ts_to_get])})      
                       ;
                    """
        try:
            cursor.execute(query,ts_to_get)
            
            result = cursor.fetchall()
        
            for row in result:
                
                x = {
                    "timestamp": row[0],
                    "entry_no":row[1],
                    "item_no":row[2],
                    "posting_date":row[3],
                    "entry_type": row[4],
                    "description": row[5],
                    "location_code": row[6],
                    "quantity": row[7],
                    "remaining_quantity": row[8],
                    "invoiced_quantity": row[9],
                    "transaction_type": row[10],
                    "country_region_code": row[11],
                    "area": row[12],
                    "order_type": row[13],
                    "completely_invoiced": row[14],
                    "shipped_qty_not_returned": row[15],
                    "return_reason_code":row[16]
                    }
                l.append(x)
            
            return l
        except pyodbc.Error as e:
        
            print(f'Error:{e}')
            return {'Error': e}