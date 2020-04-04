from dataclasses import dataclass
import os
from n41 import load_nekocabocha_chunk
from n42 import chunk2str

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def extract_dependency_noun2verb():
    for chunks in load_nekocabocha_chunk():
        for chunk in chunks:
            if chunk.dst == -1:
                continue
            if not chunk_include_pos(chunk, "名詞"):
                continue
            if not chunk_include_pos(chunks[chunk.dst], "動詞"):
                continue
            print(f"{chunk2str(chunk)}\t{chunk2str(chunks[chunk.dst])}")

def chunk_include_pos(chunk, pos) -> bool:
    return any([morph.pos == pos for morph in chunk.morphs])

if __name__ == "__main__":
    extract_dependency_noun2verb()
