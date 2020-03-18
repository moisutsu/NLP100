from n20 import load_england_text
import re

def n23():
    text = load_england_text()
    pattern = r"^(=+)([^=]+)(=+)$"
    results = re.findall(pattern, text, re.MULTILINE)
    return [(result[1], len(result[0]) - 1) for result in results]

if __name__ == "__main__":
    [print(*line) for line in n23()]

