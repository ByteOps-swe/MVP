import os.path
import re
import sys
from get_pylintScore import get_pylintScore
def get_color(score):
    if score > 9:
        return 'brightgreen'
    if score > 8:
        return 'green'
    if score > 7.5:
        return 'yellowgreen'
    if score > 6.6:
        return 'yellow'
    if score > 5.0:
        return 'orange'
    if score > 0.00:
        return 'red'
    return 'bloodred'

README_PATH = "README.md"
NUMERIC_SCORE = get_pylintScore()
BADGE_TEXT = 'PyLint'
BADGE_COLOR = get_color(float(NUMERIC_SCORE))

if not os.path.isfile(README_PATH):
    raise FileNotFoundError(f"README.md path is wrong, no file can be located at {README_PATH}")

with open(README_PATH, "r", encoding="utf8") as f:
    content = f.read()

query = f"{BADGE_TEXT}-{NUMERIC_SCORE}-{BADGE_COLOR}?logo=python&logoColor=white"
badge_url = f"https://img.shields.io/badge/{query}"

patt = r"(?<=!\[pylint]\()(.*?)(?=\))"
if re.search(patt, content) is None:
    raise ValueError("Pylint badge not found! Be sure to put an empty one which acts as a placeholder "
                     "if this is your first run. Check README.md for examples!")

result = re.sub(patt, badge_url, content)
with open(README_PATH, "w", encoding="utf8") as f:
    f.write(result)