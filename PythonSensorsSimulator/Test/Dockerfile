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
<<<<<<< HEAD
RUN pip install confluent-kafka clickhouse-connect faust pytest kafka-python pytest-asyncio mypy pylint pytest-cov

=======


RUN pip install confluent-kafka clickhouse-connect pytest kafka-python pytest-asyncio mypy pylint pytest-cov

>>>>>>> c9dbe178c3c7a2a345eb398be18e103f9570d650

CMD ["sh", "-c", "pylint --rcfile=PythonSensorsSimulator/Test/pylintrc .; mypy ./; pytest --cov-report=xml --cov=./ --capture=no ./ && cp coverage.xml /app/coverage.xml"]

#CMD ["sh", "-c", "pytest --capture=no ./Test/test_kafkaData.py"]
