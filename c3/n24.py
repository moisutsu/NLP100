from n20 import load_england_text
import re

def n24():
    text = load_england_text()
    pattern = r"^.*File:([^|]*)\|.*$"
    return re.findall(pattern, text, re.MULTILINE)

if __name__ == "__main__":
    print(*n24(), sep="\n")
