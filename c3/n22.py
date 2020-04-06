from n21 import load_england_category
import re

def extract_category_names(text) -> list:
    pattern = r"^([^|\n]+)(?:\|.+)?$"
    return re.findall(pattern, text, re.MULTILINE)

if __name__ == "__main__":
    text = "\n".join(load_england_category())
    print(*extract_category_names(text), sep="\n")
