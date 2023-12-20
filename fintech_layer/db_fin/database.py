import mariadb

class Db:
    def __init__(self,user,password,host,port,database) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

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
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
