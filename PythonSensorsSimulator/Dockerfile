FROM python:3.11-bookworm

WORKDIR /app

RUN pip install confluent-kafka

COPY . .

CMD ["python3","main.py"]