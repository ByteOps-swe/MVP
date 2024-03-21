FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install confluent-kafka==2.3.0 clickhouse-connect==0.7.2 pytest==8.0.2 kafka-python==1.4.7 pytest-asyncio==0.23.5 requests avro==1.11.3

COPY . .

CMD ["python3", "main.py"]
