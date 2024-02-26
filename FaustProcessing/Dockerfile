FROM python:3.9

WORKDIR /app

RUN pip install --upgrade faust kafka-python confluent-kafka

COPY . .

CMD ["faust", "-A", "processing", "worker", "-l", "info"]
