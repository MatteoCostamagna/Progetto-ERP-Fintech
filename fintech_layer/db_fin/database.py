import mariadb

class Db:
    """
    Class for managing the connection to a MariaDB database.

    Args:
        user (str): User name for connecting to the database.
        password (str): Password for connecting to the database.
        host (str): IP address or host name of the database server.
        port (int): Port of the database server.
        database (int): Name of the database to connect to.

    Attributes:
        user (str): User name for connecting to the database.
        password (str): Password for connecting to the database.
        host (str): IP address or host name of the database server.
        port (int): Port of the database server.
        database (int): Name of the database to connect to.
    """

    def __init__(self,user:str,password:str,host:str,port:int,database:int) -> None:
        """
        Initializes an instance of the Db class.

        Args:
            user (str): User name for connecting to the database.
            password (str): Password for connecting to the database.
            host (str): IP address or host name of the database server.
            port (int): Port of the database server.
            database (int): Name of the database to connect to.
        """
        self.user = user # Assigning the user parameter to the user attribute.
        self.password = password # Assigning the password parameter to the password attribute.
        self.host = host # Assigning the host parameter to the host attribute.
        self.port = port # Assigning the port parameter to the port attribute.
        self.database = database # Assigning the database parameter to the database attribute.
    
    #Connection to the database
    def connection(self):
        """
        Establishes a connection to the MariaDB database.

        Returns:
            mariadb.connection: A connection object if successful, else an error object.
        """
        # Initializing conn variable.
        conn = None 
        
        # Attempting to connect to the MariaDB database using provided parameters.
        try:
            conn = mariadb.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
                database = self.database
            )
            # Printing success message.
            print("Connected to the database, yay!")
            
            # Returning the connection object.
            return conn
        
        except mariadb.Error as e:
            
            # Printing error message.
            print(f"Error connecting to MariaDB Platform: {e}")
            
            # Returning the error object.
            return e
    
    # Method for creating table
    def create_table(self, table_name: str, columns: dict):
        """
        Creates a table in the MariaDB database.

        Args:
            table_name (str): Name of the table to be created.
            columns (dict): Dictionary of column names and their data types.

        Returns:
            None
        """
        #Establishing Connection to the mariadb
        conn = self.connection()
        
        #Creating the cursor for executing query
        cursor = conn.cursor()
        
        #Building the query from the given parameters(table_name,columns) 
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

        for col_name, col_type in columns.items():
            # Adding column names and types to the query.
            query += f"{col_name} {col_type}, " 

        # Removing the trailing comma and space, completing the query
        query = query[:-2] + ");"
        
        #Attempting to execute the query
        try:
            # Executing the CREATE TABLE query
            cursor.execute(query)
            # Committing the changes to the database.
            conn.commit()
        
        except mariadb.Error as e:
            
            # Printing error message.
            print(f'Error:{e}') 
        
        # Closing the cursor.
        cursor.close()
        # Closing the connection.
        conn.close()

    #Method for insert many rows in a table
    def insert_many_into_table(self, model: list[object], table_name: str):
        """
        Inserts multiple rows into a table in the MariaDB database.

        Args:
            model (list[object]): List of objects containing data to be inserted.
            table_name (str): Name of the table to insert data into.

        Returns:
            None
        """
        #Connecting to the database
        conn = self.connection()
        
        #Creating the cursor 
        cursor = conn.cursor()
        
        #Retrieving the names of the column from the first object in the list model
        columns_names = model[0].__dict__
            #Taking just the names not the value of the column from the first object
        columns_names = columns_names.keys()
        
        #Building the query
        query = f"""INSERT INTO {table_name}({",".join(columns_names)})
                    VALUES({",".join(["?" for _ in columns_names])})
                    """
        #Creating the tuple needed to pass the actual value of each column
        data_values = [tuple(x.__dict__.values()) for x in model]
        
        #Trying to execute the query
        try:
            
            cursor.executemany(query, data_values)
            conn.commit()
            print("Data added to the db")
        
        except mariadb.Error as e:
            
            print(f'Error:{e}')
        
        #Closing the connection
        finally:
            cursor.close()
            conn.close()

    def get_timestamps(self, table_name:str):
        """
        Retrieves timestamps from a specified table in the MariaDB database.

        Args:
            table_name (str): Name of the table to retrieve timestamps from.

        Returns:
            list: A list of dictionaries containing timestamps.
        """
        conn = self.connection()

        cursor = conn.cursor()

        query = f"SELECT timestamp FROM {table_name}"

        l = []
        try:
            
            cursor.execute(query)
            
            for (timestamp) in cursor:
                
                x = {"timestamp":timestamp}
                
                l.append(x)
            
            return l
        
        except mariadb.Error as e:
        
            print(f'Error:{e}')
        
        finally:
            cursor.close()
            conn.close
    
    def remove_record(self,ts_del:tuple,table_name:str):
        """
        Removes records with specified timestamps from a table in the MariaDB database.

        Args:
            ts_del (tuple): Tuple of timestamps to be deleted.
            table_name (str): Name of the table from which records will be deleted.

        Returns:
            None
        """ 
        # Establishing a connection to the MariaDB database.
        conn = self.connection()

        # Creating a cursor for executing queries.
        cursor = conn.cursor()

        # Building the DELETE query.
        query = f"""
            DELETE FROM {table_name}
            
            WHERE timestamp IN ({', '.join(['?' for _ in ts_del])});
        """
        
        # Executing the DELETE query with specified timestamps.
        try:
            cursor.execute(query,ts_del)
            # Committing the changes to the database.
            conn.commit()
        except mariadb.Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()