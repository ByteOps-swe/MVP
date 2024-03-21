FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install faust==1.10.4 kafka-python==1.4.7 confluent-kafka==2.3.0 requests avro==1.11.3

COPY . .

CMD ["faust", "-A", "processing", "worker", "-l", "info"]
