# Stage 1: Build the PythonSensorsSimulator
FROM mvp-test_base_image

WORKDIR /app
# Create directories for both PythonSensorsSimulator and FaustProcessing
RUN mkdir -p /app/PythonSensorsSimulator /app/FaustProcessing

# Copy files from PythonSensorsSimulator directory
COPY ./PythonSensorsSimulator /app/PythonSensorsSimulator

# Copy files from FaustProcessing directory
COPY ./FaustProcessing /app/FaustProcessing

COPY ./__init__.py /app/

#CMD ["sh", "-c", "pytest -p pytest_asyncio"]

CMD ["sh", "-c", "pylint --rcfile=PythonSensorsSimulator/Test/pylintrc .; pytest --cov-report=xml --cov=./ --capture=no ./ && cp coverage.xml /app/coverage.xml"]
#CMD ["sh", "-c","pytest --cov-report=xml --cov=./ --capture=no ./PythonSensorsSimulator/Test/Integration_Test/test_ClickHouseData.py && cp coverage.xml /app/coverage.xml"]
