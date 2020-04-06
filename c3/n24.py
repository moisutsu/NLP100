from n20 import load_england_text
import re

def extract_file_references(text: str) -> list:
    pattern = r"ファイル:([^|\]]+)(?:\||\])"
    return re.findall(pattern, text)

if __name__ == "__main__":
    text = load_england_text()
    print(*extract_file_references(text), sep="\n")
