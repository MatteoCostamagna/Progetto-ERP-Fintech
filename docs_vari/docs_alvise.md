Progetto ETL con Docker, FastAPI (Python) e Go
Introduzione

Il progetto ETL (Estrazione, Trasformazione e Caricamento) è stato sviluppato per gestire l'aggiornamento di dati timestampati relativi a voci di registro di capacità e articoli. Le tecnologie principali utilizzate sono Docker per la containerizzazione, Python con FastAPI per la creazione delle API e Mariadb come database. Il componente chiave dell'ETL è stato implementato in Go. È importante notare che i timestamp utilizzati nel progetto sono di tipo SQL Server Timestamp.
Scelta delle Tecnologie

Le tecnologie adottate per il progetto sono state selezionate con attenzione per garantire un ambiente efficiente e scalabile. Ecco le scelte principali:

    Docker: Utilizzato per containerizzare l'intero sistema, fornendo isolamento e facilitando la distribuzione su diversi ambienti.

    Python con FastAPI: Sono state sviluppate le API utilizzando FastAPI, un framework web veloce per Python. Questa scelta è stata motivata dalla rapidità di sviluppo offerta da Python e dalle prestazioni efficienti di FastAPI.

    Mariadb: Scelto come database per la sua affidabilità e la compatibilità con il sistema di gestione di basi di dati relazionali.

    Go: La parte principale dell'ETL è stata scritta in Go. La scelta di Go è stata determinata dalla sua facilità di apprendimento, velocità di compilazione rapida e supporto nativo per la concorrenza, che si è rivelato fondamentale per eseguire chiamate API in modo simultaneo.

Implementazione del Progetto
Creazione delle API con FastAPI (Python)

Inizialmente, sono state create le API in Python utilizzando FastAPI. Queste API erano responsabili di fornire i timestamp SQL Server, recuperare i dati dal database e gestire le richieste di eliminazione e caricamento.
Scrittura del Programma ETL in Go

Il componente principale del processo ETL è stato implementato in Go. Questo programma Go è responsabile di eseguire le operazioni di confronto, eliminazione e caricamento dei dati, considerando i timestamp di tipo SQL Server. La scelta di Go ha permesso di sfruttare efficacemente la concorrenza, rendendo possibile eseguire chiamate API contemporaneamente e ottenere prestazioni superiori rispetto a Python.
Schedulazione delle Run

Il programma Go è schedulato per eseguire automaticamente ogni giorno alle 23:30. Questo assicura che le operazioni di ETL vengano eseguite regolarmente, garantendo l'aggiornamento quotidiano dei dati.
Vantaggi di Go

    Facilità di Apprendimento: Go è noto per la sua sintassi semplice e intuitiva, rendendolo facile da apprendere.

    Velocità di Compilazione: La compilazione rapida di Go è un vantaggio, consentendo un rapido ciclo di sviluppo.

    Concorrenza: Il supporto nativo per la concorrenza in Go è stato sfruttato per eseguire chiamate API in parallelo, migliorando le prestazioni complessive del programma.

    Containerizzazione: Go è facilmente containerizzabile, semplificando la distribuzione e la gestione dell'applicazione in ambienti Docker.

Conclusioni

Il progetto ETL, implementato con Docker, FastAPI in Python e Go, ha permesso di realizzare un sistema efficiente e scalabile per la gestione dei dati timestampati di tipo SQL Server. L'utilizzo combinato di queste tecnologie ha consentito di sfruttare al meglio le caratteristiche di ciascuna, garantendo un'applicazione robusta e performante, con esecuzioni pianificate giornalmente alle 23:30.