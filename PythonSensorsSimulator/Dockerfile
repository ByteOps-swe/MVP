FROM python:3.9

WORKDIR /app

RUN pip install confluent-kafka clickhouse-connect pytest kafka-python pytest-asyncio

COPY . .

CMD ["python3", "main.py"]
