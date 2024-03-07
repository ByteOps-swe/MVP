# Stage 1: Build the PythonSensorsSimulator
FROM python:3.9
# Create directories for both PythonSensorsSimulator and FaustProcessing
RUN mkdir -p /app/PythonSensorsSimulator /app/FaustProcessing

# Copy files from PythonSensorsSimulator directory
COPY ./PythonSensorsSimulator /app/PythonSensorsSimulator

# Copy files from FaustProcessing directory
COPY ./FaustProcessing /app/FaustProcessing


RUN pip install confluent-kafka clickhouse-connect pytest kafka-python pytest-asyncio mypy pylint pytest-cov

COPY . .

CMD ["sh", "-c", "pylint --rcfile=PythonSensorsSimulator/Test/pylintrc .; mypy ./; pytest --cov-report=xml --cov=./ --capture=no ./ && cp coverage.xml /app/coverage.xml"]

#CMD ["sh", "-c", "pytest --capture=no ./Test/test_kafkaData.py"]
