import pyodbc

class Db:
    """
    Class for interacting with a database using the pyodbc module.

    Args:
        connection_string (str): The connection string required to connect to the database.

    Attributes:
        connection_string (str): The connection string used for connecting to the database.

    Methods:
        __init__(connection_string: str): Constructor of the class, initializes the connection string.
        
    """
    def __init__(self, connection_string: str):
        """
        Constructor of the Db class.

        Args:
            connection_string (str): The connection string required to connect to the database.
        """
        self.connection_string = connection_string

    def connection(self):
        """
        Returns a database connection object using the connection string.

        Returns:
            pyodbc.Connection or None: A database connection object, or None in case of an error.

        Notes:
            The method handles any connection errors and prints the error in case of failure.
        """
        
        conn = None
        
        try:
            # Tries to establish a connection to the database using the provided connection string 
            conn = pyodbc.connect(self.connection_string, autocommit=True)
        
        except pyodbc.Error as e:
           # In case of an error during the connection, prints the error     
            print(e)
        
        return conn

    def get_capacity(self):
        """
        Retrieves data from the '$Capacity Ledger Entry$' table of the database and returns a list of dictionaries.

        Returns:
            list: A list of dictionaries containing data retrieved from the table.
            
        Notes:
            - Uses the `connection` method to get a database connection object.
            - Executes an SQL query on the table and converts the results into a list of dictionaries.
            - Data from the table is converted into dictionaries with meaningful keys.
            - Values of numeric columns are converted to float.
            - Handles any errors during connection or query execution, returning an empty list in case of failure.
        """

        l = []
        
        # Gets a database connection object
        conn = self.connection()
        
        # Creates a cursor to execute queries
        cursor = conn.cursor()
        
        # Executes an SQL query on the '$Capacity Ledger Entry$' table
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
                        [Scrap Quantity],
                        [Operation No_]
                    FROM
                        [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972]
                    ;
                    """)
    
        # Gets all the results of the query
        result = cursor.fetchall()
    
        for row in result:
        # Converts the results into a dictionary and adds them to the list
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
                "scrap_quantity": float(row[12]),
                "operation_no":row[13]
                }
        
            l.append(x)
    
        return l
    
    def get_item(self):
        """
        Retrieves data from the '$Item Ledger Entry$' table of the database and returns a list of dictionaries.

        Returns:
            list: A list of dictionaries containing data retrieved from the table.
            
        Notes:
            - Uses the `connection` method to get a database connection object.
            - Executes an SQL query on the table and converts the results into a list of dictionaries.
            - Data from the table is converted into dictionaries with meaningful keys.
            - Handles any errors during connection or query execution, returning an empty list in case of failure.
        """
        l = []
        
        # Gets a database connection object
        conn = self.connection()
        
        # Creates a cursor to execute queries
        cursor = conn.cursor()

        # Executes an SQL query on the '$Item Ledger Entry$' table
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
        # Gets all the results of the query
        result = cursor.fetchall()
    
        for row in result:
            # Converts the results into a dictionary and adds them to the list
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
        """
        Retrieves timestamps from the '$Capacity Ledger Entry$' table of the database and returns a list of dictionaries.

        Returns:
            list: A list of dictionaries containing timestamps retrieved from the table.
            
        Notes:
            - Uses the `connection` method to get a database connection object.
            - Executes an SQL query to obtain timestamps from the table.
            - Returns a list of dictionaries with the key "timestamp".
            - Handles any errors during connection or query execution, returning a dictionary with the key "Error" in case of failure.
        """
        # Gets a database connection object
        conn = self.connection()

        # Creates a cursor to execute queries
        cursor = conn.cursor()

        # SQL query to obtain timestamps from the '$Capacity Ledger Entry$' table
        query = f"SELECT convert(bigint,[timestamp]) FROM [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];"

        l = []
        
        try:
            
            # Executes the SQL query
            cursor.execute(query)
            
            # Iterates over the results and adds the timestamps to the list
            for row in cursor:
                
                x = {"timestamp":row[0]}
                
                l.append(x)
            
            return l
        
        except pyodbc.Error as e:
            # Handles connection or query execution errors, returning a dictionary with the key "Error"
            print(f'Error:{e}')
            return {'Error': e}
            
    def get_timestamps_item(self):
        """
        Retrieves timestamps from the '$Item Ledger Entry$' table of the database and returns a list of dictionaries.

        Returns:
            list: A list of dictionaries containing timestamps retrieved from the table.
            
        Notes:
            - Uses the `connection` method to get a database connection object.
            - Executes an SQL query to obtain timestamps from the table.
            - Returns a list of dictionaries with the key "timestamp".
            - Handles any errors during connection or query execution, returning a dictionary with the key "Error" in case of failure.
        """
        # Gets a database connection object
        conn = self.connection()

        # Creates a cursor to execute queries
        cursor = conn.cursor()

        # SQL query to obtain timestamps from the '$Item Ledger Entry$' table
        query = f"SELECT convert(bigint,[timestamp]) FROM [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Item Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];"

        l = []
        
        try:
            # Executes the SQL query
            cursor.execute(query)
            
            # Iterates over the results and adds the timestamps to the list
            for row in cursor:
                
                x = {"timestamp":row[0]}
                
                l.append(x)
            
            return l
        
        except pyodbc.Error as e:
            # Handles connection or query execution errors, returning a dictionary with the key "Error"
            print(f'Error:{e}')
            return {'Error': e}
        
    def get_capacity_by_ts(self, ts_to_get):
        """
        Retrieves data from the '$Capacity Ledger Entry$' table of the database for specific timestamps and returns a list of dictionaries.

        Args:
            ts_to_get (tuple): A tuple of timestamps for which to retrieve the data.

        Returns:
            list: A list of dictionaries containing data retrieved from the table for the specified timestamps.

        Notes:
            - Uses the `connection` method to get a database connection object.
            - Executes an SQL query on the table, filtering the results for the specified timestamps.
            - Returns a list of dictionaries with meaningful keys.
            - Values of numeric columns are converted to float.
            - Handles any errors during connection, query execution, or data conversion, returning an empty list in case of failure.
        """
        l = []
        
        # Gets a database connection object
        conn = self.connection()
        
        # Creates a cursor to execute queries
        cursor = conn.cursor()

        # SQL query to obtain data from the '$Capacity Ledger Entry$' table for specific timestamps
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
                        [Scrap Quantity],
                        [Operation No_]
                    FROM
                        [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972]
                WHERE 
                    convert(bigint,[timestamp]) IN  ({', '.join(["?" for _ in ts_to_get])})
                       ;
                    """
        try:
            # Execute the quey with the specified timestamps
            cursor.execute(query,ts_to_get)
            result = cursor.fetchall()
        
            for row in result:
                # Converts the results into a dictionary and appends them to the list
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
                    "scrap_quantity": float(row[12]),
                    "operation_no":row[13]
                    }
                l.append(x)
            
            return l
        except pyodbc.Error as e:
            # Handles errors in connection, query execution, or data conversion, returning an empty list
            print(f'Error:{e}')
            return []

    
    def get_item_by_ts(self,ts_to_get:tuple):
        """
    Retrieves data from the '$Item Ledger Entry$' table of the database for specific timestamps and returns a list of dictionaries.

    Args:
        ts_to_get (tuple): A tuple of timestamps for which to retrieve the data.

    Returns:
        list: A list of dictionaries containing data retrieved from the table for the specified timestamps.

    Notes:
        - Uses the `connection` method to get a database connection object.
        - Executes an SQL query on the table, filtering the results for the specified timestamps.
        - Returns a list of dictionaries with meaningful keys.
        - Handles any errors during connection, query execution, or data conversion, returning an empty list in case of failure.
    """
        l = []
        
        # Gets a database connection object
        conn = self.connection()
        
        # Creates a cursor to execute queries
        cursor = conn.cursor()

        # SQL query to obtain data from the '$Item Ledger Entry$' table for specific timestamps
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
            # Executes the SQL query with the specified timestamps
            cursor.execute(query,ts_to_get)
            
            result = cursor.fetchall()
        
            for row in result:
                # Converts the results into a dictionary and appends them to the list
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
            # Handles errors in connection, query execution, or data conversion, returning an empty list
            print(f'Error:{e}')
            return []