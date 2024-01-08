import mariadb

class Db:
    def __init__(self,user:str,password:str,host:str,port:int,database:int) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
    
    #Connection to the database
    def connection(self):
        
        conn = None
        
        try:
            conn = mariadb.connect(
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port,
                database = self.database
            )
            
            print("Connected to the database, yay!")
            
            return conn
        
        except mariadb.Error as e:
            
            print(f"Error connecting to MariaDB Platform: {e}")
            
            return e
    
    # Method for creating table
    def create_table(self, table_name: str, columns: dict):
        
        #Establishing Connection to the mariadb
        conn = self.connection()
        
        #Creating the cursor for executing query
        cursor = conn.cursor()
        
        #Building the query from the given parameters(table_name,columns) 
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

        for col_name, col_type in columns.items():
            query += f"{col_name} {col_type}, "

        query = query[:-2] + ");"
        
        #Attempting to execute the query
        try:
            
            cursor.execute(query)
            conn.commit()
        
        except mariadb.Error as e:
            
            print(f'Error:{e}')
        
        #Closing the connection no matter if query has gone well
        cursor.close()
        conn.close()

    #Method for insert many rows in a table
    def insert_many_into_table(self, model: list[object], table_name: str):
        
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

        conn = self.connection()

        cursor = conn.cursor()

        query = f"""
            DELETE FROM {table_name}
            
            WHERE timestamp IN ({', '.join(['?' for _ in ts_del])});
        """

        try:
            cursor.execute(query,ts_del)
        except mariadb.Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()