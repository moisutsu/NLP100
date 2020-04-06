from n20 import load_england_text
import re

def get_session_level(text) -> list:
    pattern = r"('+)([^']+)'+"
    results = re.findall(pattern, text, re.MULTILINE)
    return [(result[1], len(result[0])) for result in results]

if __name__ == "__main__":
    text = load_england_text()
    [print(f"Session name: {line[0]}, Level: {line[1]}") for line in get_session_level(text)]
