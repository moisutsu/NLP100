from dataclasses import dataclass
import os
from n41 import load_nekocabocha_chunk

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def extract_dependency():
    for chunks in load_nekocabocha_chunk():
        for chunk in chunks:
            if chunk.dst == -1:
                continue
            print(f"{chunk2str(chunk)}\t{chunk2str(chunks[chunk.dst])}")

# Chunkを記号を含まない文字列に変更
def chunk2str(chunk):
    return "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])

if __name__ == "__main__":
    extract_dependency()
