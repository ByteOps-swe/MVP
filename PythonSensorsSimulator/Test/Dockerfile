FROM python:3.9

WORKDIR /app

RUN pip install confluent-kafka clickhouse-connect pytest kafka-python pytest-asyncio mypy pylint coveralls pytest-cov

COPY . .

CMD ["sh", "-c", "pylint --rcfile=Test/pylintrc .; mypy Model/; pytest --cov-report=xml --cov=./ --capture=no ./; tail -f /dev/null"]

