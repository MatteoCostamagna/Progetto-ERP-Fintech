import pyodbc

class Db:
    """
    Classe per interagire con un database utilizzando il modulo pyodbc.

    Args:
        connection_string (str): La stringa di connessione necessaria per connettersi al database.

    Attributes:
        connection_string (str): La stringa di connessione utilizzata per la connessione al database.

    Methods:
        __init__(connection_string: str): Costruttore della classe, inizializza la stringa di connessione.
        
    """
    def __init__(self, connection_string: str):
        """
        Costruttore della classe Db.

        Args:
            connection_string (str): La stringa di connessione necessaria per connettersi al database.
        """
        self.connection_string = connection_string

    def connection(self):
        """
        Restituisce un oggetto di connessione al database utilizzando la stringa di connessione.

        Returns:
            pyodbc.Connection or None: Un oggetto di connessione al database, o None in caso di errore.

        Notes:
            Il metodo gestisce eventuali errori di connessione e stampa l'errore in caso di fallimento.
        """
        
        conn = None
        
        try:
            # Tenta di stabilire una connessione al database utilizzando la stringa di connessione fornita 
            conn = pyodbc.connect(self.connection_string, autocommit=True)
        
        except pyodbc.Error as e:
         # In caso di errore durante la connessione, stampa l'errore       
            print(e)
        
        return conn

    def get_capacity(self):
        """
        Recupera dati dalla tabella '$Capacity Ledger Entry$' del database e restituisce una lista di dizionari.

        Returns:
            list: Una lista di dizionari contenenti i dati recuperati dalla tabella.
            
        Notes:
            - Utilizza il metodo `connection` per ottenere un oggetto di connessione al database.
            - Esegue una query SQL sulla tabella e converte i risultati in una lista di dizionari.
            - I dati della tabella sono convertiti in dizionari con chiavi significative.
            - I valori delle colonne numeriche vengono convertiti in float.
            - Gestisce eventuali errori durante la connessione o l'esecuzione della query, restituendo una lista vuota in caso di fallimento.
        """

        l = []
        
        # Ottiene un oggetto di connessione al database
        conn = self.connection()
        
        # Crea un cursore per eseguire query
        cursor = conn.cursor()
        
        # Esegue una query SQL sulla tabella '$Capacity Ledger Entry$'
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
    
        # Ottiene tutti i risultati della query
        result = cursor.fetchall()
    
        for row in result:
        # Converte i risultati in un dizionario e li aggiunge alla lista
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
        """
        Recupera dati dalla tabella '$Item Ledger Entry$' del database e restituisce una lista di dizionari.

        Returns:
            list: Una lista di dizionari contenenti i dati recuperati dalla tabella.
            
        Notes:
            - Utilizza il metodo `connection` per ottenere un oggetto di connessione al database.
            - Esegue una query SQL sulla tabella e converte i risultati in una lista di dizionari.
            - I dati della tabella sono convertiti in dizionari con chiavi significative.
            - Gestisce eventuali errori durante la connessione o l'esecuzione della query, restituendo una lista vuota in caso di fallimento.
        """
        l = []
        
        # Ottiene un oggetto di connessione al database
        conn = self.connection()
        
        # Crea un cursore per eseguire query
        cursor = conn.cursor()

        # Esegue una query SQL sulla tabella '$Item Ledger Entry$'
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
        # Ottiene tutti i risultati della query
        result = cursor.fetchall()
    
        for row in result:
            # Converte i risultati in un dizionario e li aggiunge alla lista
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
        Recupera i timestamp dalla tabella '$Capacity Ledger Entry$' del database e restituisce una lista di dizionari.

        Returns:
            list: Una lista di dizionari contenenti i timestamp recuperati dalla tabella.
            
        Notes:
            - Utilizza il metodo `connection` per ottenere un oggetto di connessione al database.
            - Esegue una query SQL per ottenere i timestamp dalla tabella.
            - Restituisce una lista di dizionari con chiave "timestamp".
            - Gestisce eventuali errori durante la connessione o l'esecuzione della query, restituendo un dizionario con la chiave "Error" in caso di fallimento.
        """
        
        conn = self.connection()

        # Crea un cursore per eseguire query
        cursor = conn.cursor()

        # Query SQL per ottenere i timestamp dalla tabella '$Capacity Ledger Entry$'
        query = f"SELECT convert(bigint,[timestamp]) FROM [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Capacity Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];"

        l = []
        
        try:
            
            # Esegue la query SQL
            cursor.execute(query)
            
            # Itera sui risultati e aggiunge i timestamp alla lista
            for row in cursor:
                
                x = {"timestamp":row[0]}
                
                l.append(x)
            
            return l
        
        except pyodbc.Error as e:
            # Gestisce gli errori di connessione o esecuzione della query, restituendo un dizionario con la chiave "Error"
            print(f'Error:{e}')
            return {'Error': e}
            
    def get_timestamps_item(self):
        """
        Recupera i timestamp dalla tabella '$Item Ledger Entry$' del database e restituisce una lista di dizionari.

        Returns:
            list: Una lista di dizionari contenenti i timestamp recuperati dalla tabella.
            
        Notes:
            - Utilizza il metodo `connection` per ottenere un oggetto di connessione al database.
            - Esegue una query SQL per ottenere i timestamp dalla tabella.
            - Restituisce una lista di dizionari con chiave "timestamp".
            - Gestisce eventuali errori durante la connessione o l'esecuzione della query, restituendo un dizionario con la chiave "Error" in caso di fallimento.
        """
        conn = self.connection()

        # Crea un cursore per eseguire query
        cursor = conn.cursor()

        # Query SQL per ottenere i timestamp dalla tabella '$Item Ledger Entry$'
        query = f"SELECT convert(bigint,[timestamp]) FROM [Demo Database BC (21-0)].[dbo].[CRONUS Italia S_p_A_$Item Ledger Entry$437dbf0e-84ff-417a-965d-ed2bb9650972];"

        l = []
        
        try:
            # Esegue la query SQL
            cursor.execute(query)
            
            # Itera sui risultati e aggiunge i timestamp alla lista
            for row in cursor:
                
                x = {"timestamp":row[0]}
                
                l.append(x)
            
            return l
        
        except pyodbc.Error as e:
            # Gestisce gli errori di connessione o esecuzione della query, restituendo un dizionario con la chiave "Error"
            print(f'Error:{e}')
            return {'Error': e}
        
    def get_capacity_by_ts(self, ts_to_get):
        """
        Recupera dati dalla tabella '$Capacity Ledger Entry$' del database per timestamp specifici e restituisce una lista di dizionari.

        Args:
            ts_to_get (tuple): Una tupla di timestamp per cui recuperare i dati.

        Returns:
            list: Una lista di dizionari contenenti i dati recuperati dalla tabella per i timestamp specificati.

        Notes:
            - Utilizza il metodo `connection` per ottenere un oggetto di connessione al database.
            - Esegue una query SQL sulla tabella filtrando i risultati per i timestamp specificati.
            - Restituisce una lista di dizionari con chiavi significative.
            - I valori delle colonne numeriche vengono convertiti in float.
            - Gestisce eventuali errori durante la connessione, l'esecuzione della query o la conversione dei dati, restituendo una lista vuota in caso di fallimento.
        """
        l = []
        
        # Ottiene un oggetto di connessione al database
        conn = self.connection()
        
        # Crea un cursore per eseguire query
        cursor = conn.cursor()

        # Query SQL per ottenere i dati dalla tabella '$Capacity Ledger Entry$' per i timestamp specificati
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
            # Esegue la query SQL con i timestamp specificati
            cursor.execute(query,ts_to_get)
            result = cursor.fetchall()
        
            for row in result:
                # Converte i risultati in un dizionario e li aggiunge alla lista
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
            # Gestisce gli errori di connessione, esecuzione della query o conversione dei dati, restituendo una lista vuota
            print(f'Error:{e}')
            return []

    
    def get_item_by_ts(self,ts_to_get:tuple):
        """
        Recupera dati dalla tabella '$Item Ledger Entry$' del database per timestamp specifici e restituisce una lista di dizionari.

        Args:
            ts_to_get (tuple): Una tupla di timestamp per cui recuperare i dati.

        Returns:
            list: Una lista di dizionari contenenti i dati recuperati dalla tabella per i timestamp specificati.

        Notes:
            - Utilizza il metodo `connection` per ottenere un oggetto di connessione al database.
            - Esegue una query SQL sulla tabella filtrando i risultati per i timestamp specificati.
            - Restituisce una lista di dizionari con chiavi significative.
            - Gestisce eventuali errori durante la connessione, l'esecuzione della query o la conversione dei dati, restituendo una lista vuota in caso di fallimento.
        """
        l = []
        
        # Ottiene un oggetto di connessione al database
        conn = self.connection()
        
        # Crea un cursore per eseguire query
        cursor = conn.cursor()

        # Query SQL per ottenere i dati dalla tabella '$Item Ledger Entry$' per i timestamp specificati
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
            # Esegue la query SQL con i timestamp specificati
            cursor.execute(query,ts_to_get)
            
            result = cursor.fetchall()
        
            for row in result:
                # Converte i risultati in un dizionario e li aggiunge alla lista
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
            # Gestisce gli errori di connessione, esecuzione della query o conversione dei dati, restituendo una lista vuota
            print(f'Error:{e}')
            return []