import CaboCha
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "neko.txt"
OUTPUT_FILE_NAME = "neko.txt.cabocha"

sentence = ""
with open(INPUT_FILE_NAME) as f:
    sentences = f.readlines()

c = CaboCha.Parser()
with open(OUTPUT_FILE_NAME, mode="w") as f:
    for sentence in sentences:
        tree = c.parse(sentence)
        f.write(tree.toString(CaboCha.FORMAT_LATTICE))
