import os.path
import re

def get_pylintScore(file = "pylint_output.txt"):
    content = ""

    # Read the pylint output file and raise an error if it does not exist
    if not os.path.isfile(file):
        raise FileNotFoundError(f"Pylint output file not found at {file}")

    with open(file, "r", encoding="utf16") as f:
        content = f.read()

    # Extract the score from the pylint output by looking fo the patter: Your code has been rated at 9.83/10 (previous run: 9.83/10, +0.00)
    pattern = r"(?<=rated at )(\d+\.\d+)"
    match = re.search(pattern, content)

    return match.group(0)