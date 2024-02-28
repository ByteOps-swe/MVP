FROM python:3.9

WORKDIR /app

RUN pip install confluent-kafka clickhouse-driver pytest faust pytest-asyncio

COPY . .

CMD ["python3", "main.py"]
#CMD ["python3", "testScript.py"]