# Stage 1: Build the PythonSensorsSimulator
FROM python:3.9 AS python_simulator

WORKDIR /app/PythonSensorsSimulator
COPY ./PythonSensorsSimulator .

# Stage 2: Build the FaustProcessing
FROM python:3.9 AS faust_processing

WORKDIR /app/FaustProcessing
COPY ./FaustProcessing .

# Stage 3: Final container
FROM python:3.9

WORKDIR /app

# Copy files from both previous stages
COPY --from=python_simulator /app/PythonSensorsSimulator /app/PythonSensorsSimulator
COPY --from=faust_processing /app/FaustProcessing /app/FaustProcessing

RUN pip install confluent-kafka clickhouse-connect pytest kafka-python pytest-asyncio mypy pylint pytest-cov

COPY . .

CMD ["sh", "-c", "pylint --rcfile=Test/pylintrc .; mypy Model/; pytest --cov-report=xml --cov=./ --capture=no ./ && cp coverage.xml /app/coverage.xml"]

#CMD ["sh", "-c", "pytest --capture=no ./Test/test_kafkaData.py"]
