import MeCab
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "neko.txt"
OUTPUT_FILE_NAME = "neko.txt.mecab"

text = ""
with open(INPUT_FILE_NAME) as f:
    text = f.read()

t = MeCab.Tagger("")
with open(OUTPUT_FILE_NAME, mode = "w") as f:
    f.write(t.parse(text))
