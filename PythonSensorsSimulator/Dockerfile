FROM python:3.11-bookworm

WORKDIR /app

RUN pip install confluent-kafka faust

COPY . .

CMD ["python3", "main.py"]