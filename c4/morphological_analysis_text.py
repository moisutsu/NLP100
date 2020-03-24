import MeCab
import os

INPUT_FILE_NAME = "neko.txt"
OUTPUT_FILE_NAME = "neko.txt.mecab"
CURRENT_DIR_NAME = os.path.dirname(__file__)

text = ""
with open(os.path.join(CURRENT_DIR_NAME, INPUT_FILE_NAME)) as f:
    text = f.read()

t = MeCab.Tagger("")
with open(os.path.join(CURRENT_DIR_NAME, OUTPUT_FILE_NAME), mode = "w") as f:
    f.write(t.parse(text))
