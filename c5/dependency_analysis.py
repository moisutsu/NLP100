import CaboCha
import os

INPUT_FILE_NAME = "neko.txt"
OUTPUT_FILE_NAME = "neko.txt.cabocha"
CURRENT_DIR_NAME = os.path.dirname(__file__)

sentence = ""
with open(os.path.join(CURRENT_DIR_NAME, INPUT_FILE_NAME), encoding="utf-8") as f:
    sentences = f.readlines()

c = CaboCha.Parser()
with open(os.path.join(CURRENT_DIR_NAME, OUTPUT_FILE_NAME), mode="w", encoding="utf-8") as f:
    for sentence in sentences:
        tree = c.parse(sentence)
        f.write(tree.toString(CaboCha.FORMAT_LATTICE))
