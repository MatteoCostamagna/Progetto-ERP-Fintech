import pyodbc

server = '127.0.0.1,1433'
database = 'Demo Database BC (21-0)'
username = 'sa'
password = '/Ferrari499p'
driver = 'ODBC Driver 17 for SQL Server'  # Use the appropriate driver name

# Construct the connection string
connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish the connection
try:
    connection = pyodbc.connect(connection_string)
    print('Connected to the database!')
except pyodbc.Error as e:
    print(f'Error connecting to the database: {e}')
