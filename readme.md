
# Progetto Fintech-ERP

Benvenuto nel repository del progetto Fintech-ERP! Questo progetto è basato su un'architettura Docker per creare un ambiente Python con un driver per la connessione a SQL Server. Il container Python espone API utili per recuperare i dati da caricare nel sistema.

## Istruzioni per l'uso

### 1. Build dell'immagine Docker

Posizionati da terminale nella stessa cartella del Dockerfile e esegui il seguente comando:

```bash
docker build -t prj-finerp-image .
``` 
### 2. Creazione della rete Docker

È necessario creare una rete Docker di tipo bridge affinché il container Python possa comunicare con SQL Server. 

Esegui il seguente comando:
```bash
docker network create -d bridge etl-network
```

### 3. Run del container Python

Esegui il container Python con il seguente comando:
```bash
docker run --network etl-network --name prj-finerp-container -p 80:80 -d -v ${pwd}:/code prj-finerp-image
```

### 4. Configurazione di SQL Server

Per quanto riguarda SQL Server, segui i passaggi seguenti:

Pull dell'immagine da Docker Hub
```bash
docker pull alvaise/fintech_erp:latest
```
Run del container SQL Server

Esegui il container SQL Server con il seguente comando:
```bash
docker run --name sql-server-container --network etl-network -p 1433:1433 alvaise/fintech_erp:latest
```


