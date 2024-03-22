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


CMD ["sh", "-c", "pylint --rcfile=PythonSensorsSimulator/Test/pylintrc  --output-format=parseable . > pylint_output.txt; pytest -c PythonSensorsSimulator/Test/pytest.ini --cov-report=xml --cov-config=.coveragerc --cov=./ --capture=no && cp coverage.xml /app/coverage.xml"]
#CMD ["sh", "-c","pytest --cov-report=xml --cov=./ --capture=no ./PythonSensorsSimulator/Test/SystemTest/TS_performance.py && cp coverage.xml /app/coverage.xml"]
# CMD ["sh", "-c", "pylint --rcfile=PythonSensorsSimulator/Test/pylintrc  --output-format=parseable . > pylint_output.txt"]
