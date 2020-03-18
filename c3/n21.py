from n20 import load_england_text
import re

def n21():
    text = load_england_text()
    pattern = r"^.*Category.*$"
    return re.findall(pattern, text, re.MULTILINE)

if __name__ == "__main__":
    print(*n21(), sep="\n")
