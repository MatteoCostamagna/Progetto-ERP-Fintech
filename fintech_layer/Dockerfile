#Dockerfile per ambiente python fintech-db
FROM python:3.10-slim

WORKDIR /code

COPY ./db_fin ./db_fin

COPY ./requirements_api_mdb.txt ./

RUN apt-get update && apt-get install -y libmariadb-dev gcc

RUN pip install --no-cache-dir -r requirements_api_mdb.txt

ENV PYTHONPATH="${PYTHONPATH}:/code/db_fin"

CMD [ "uvicorn","db_fin.api_mdb:app", "--host", "0.0.0.0", "--port", "90", "--reload" ]