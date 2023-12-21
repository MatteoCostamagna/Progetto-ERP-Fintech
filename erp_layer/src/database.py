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

    def create_table(self, table_name: str, columns: dict):
        conn = self.connection()
        cursor = conn.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("

        for col_name, col_type in columns.items():
            query += f"{col_name} {col_type}, "

        query = query[:-2] + ")"
        cursor.execute(query)
        conn.commit()
        conn.close()

    def insert_into_table(self, model: object, table_name: str):
        conn = self.connection()
        cursor = conn.cursor()
        columns_names = model.__dict__
        #columns_names.pop('id')
        columns_names = columns_names.keys()
        query = f"""INSERT INTO {table_name}({",".join(columns_names)})
            VALUES({",".join(["?" for _ in columns_names])})
            """
        data_values = tuple(model.__dict__.values())
        cursor.execute(query, data_values)
        conn.commit()
        conn.close()

    def insert_many_into_table(self, model: list[object], table_name: str):
        conn = self.connection()
        cursor = conn.cursor()
        columns_names = model[0].__dict__
        #columns_names.pop('id')
        columns_names = columns_names.keys()
        query = f"""INSERT INTO {table_name}({",".join(columns_names)})
                    VALUES({",".join(["?" for _ in columns_names])})
                    """
        data_values = [tuple(x.__dict__.values()) for x in model]
        cursor.executemany(query, data_values)
        conn.commit()
        conn.close()

    def drop_table(self, table_name: str):
        conn = self.connection()
        cursor = conn.cursor()
        query = f"""DROP TABLE {table_name}"""
        cursor.execute(query)
        conn.commit()
        conn.close()

    """ def select_one(self, table_name: str):
        conn = self.connection()
        conn.row_factory = sqlite3.Row
        res = conn.execute(f'SELECT * FROM {table_name}')
        results = res.fetchone()
        conn.commit()
        conn.close()
        return results """

    """ def get_all_by_table(self, table_name: str):
        conn = self.connection()
        conn.row_factory = sqlite3.Row
        res = conn.execute(f'SELECT * FROM {table_name}')
        results = res.fetchall()
        conn.commit()
        conn.close()
        return results """

    def delete_from_table_by_id(self, table_name: str, id: int):
        conn = self.connection()
        cursor = conn.cursor()
        query = f"""DELETE FROM {table_name} WHERE id = ?"""
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
    def get_capacity(self):
        conn = self.connection()
        cursor = conn.cursor()
        query = """SELECT
                        [timestamp],
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
                    """
        res = cursor.execute(query)
        results = res.fetchall()
        return results
    def get_item(self):
        conn = self.connection()
        cursor = conn.cursor()
        query = """SELECT
                    [timestamp],
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
                    """
        res = cursor.execute(query)
        results = res.fetchall()
        conn.close()
        return results