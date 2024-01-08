#Dockerfile per Python API SQL Server

# Utilizza un'immagine leggera di Python 3.10 come base
FROM python:3.10-slim-buster

# Installa pacchetti necessari per la gestione degli aggiornamenti e delle chiavi
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https gnupg2 curl ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Aggiunge la chiave di Microsoft per scaricare i pacchetti MS SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -


# Aggiunge il repository dei pacchetti MS SQL Server al file delle sorgenti
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list


# Aggiorna le informazioni del repository e installa il driver ODBC di MS SQL Server
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Imposta la directory di lavoro come /code
WORKDIR /code


# Copia la directory src (contenente il codice sorgente) nel contesto dell'immagine
COPY ./src ./src


# Copia il file requirements.txt nel contesto dell'immagine
COPY ./requirements.txt ./


# Installa le dipendenze Python elencate in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Imposta la variabile di ambiente PYTHONPATH per includere la directory /code/src
ENV PYTHONPATH="${PYTHONPATH}:/code/src"


# Comando predefinito per eseguire l'applicazione FastAPI con Uvicorn
CMD [ "uvicorn","src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]