FROM python:3.11-bookworm

WORKDIR /app

RUN pip install confluent-kafka clickhouse-driver 

COPY . .

CMD ["python3", "main.py"]
#CMD ["python3", "testScript.py"]