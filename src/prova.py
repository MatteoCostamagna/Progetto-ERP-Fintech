import pyodbc

server = 'sql-server-container'
database = 'Demo Database BC (21-0)'
username = 'SA'
password = '/Ferrari499p'
driver = 'ODBC Driver 17 for SQL Server'  # Use the appropriate driver name

# Construct the connection string
connection_string = f'driver={driver};server={server};database={database};uid={username};pwd={password}'


# Establish the connection
try:
    connection = pyodbc.connect(connection_string)
    print('Connected to the database!')
except pyodbc.Error as e:
    print(f'Error connecting to the database: {e}')