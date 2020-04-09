from n20 import load_england_text
import re

def get_category_names(text: str) -> list:
    pattern = r"^\[\[Category:([^|\]]+)(?:\|.+)?]]$"
    return re.findall(pattern, text, re.MULTILINE)

if __name__ == "__main__":
    text = load_england_text()
    print(*get_category_names(text), sep="\n")
