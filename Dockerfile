FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-transport-https gnupg2 curl ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY ./src ./src

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn","src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]