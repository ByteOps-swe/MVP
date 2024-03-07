FROM python:3.9

WORKDIR /app

RUN pip install confluent-kafka clickhouse-connect pytest kafka-python pytest-asyncio mypy pylint pytest-cov

COPY . .

#CMD ["sh", "-c", "pylint --rcfile=Test/pylintrc .; mypy Model/; pytest --cov-report=xml --cov=./ --capture=no ./ && cp coverage.xml /app/coverage.xml"]

CMD ["sh", "-c", "pytest --capture=no ./Test/test_Clickhouse_tmp_table.py"]
