# Stage 1: Build the PythonSensorsSimulator
FROM python:3.9

WORKDIR /app
# Create directories for both PythonSensorsSimulator and FaustProcessing
RUN mkdir -p /app/PythonSensorsSimulator /app/FaustProcessing

# Copy files from PythonSensorsSimulator directory
COPY ./PythonSensorsSimulator /app/PythonSensorsSimulator

# Copy files from FaustProcessing directory
COPY ./FaustProcessing /app/FaustProcessing

COPY ./__init__.py /app/

RUN pip install confluent-kafka clickhouse-connect faust pytest kafka-python pytest-asyncio mypy pylint pytest-cov


#CMD ["sh", "-c", "pylint --rcfile=PythonSensorsSimulator/Test/pylintrc .; mypy ./; pytest --cov-report=xml --cov=./ --capture=no ./ && cp coverage.xml /app/coverage.xml"]

CMD ["sh", "-c", "pytest --capture=no ./Test/test_HealthModelIntegration.py"]
