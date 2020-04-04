import os
from n41 import load_nekocabocha_chunk
from n42 import chunk2str
from n43 import chunk_include_pos

OUTPUT_FILE_NAME = "verb_case_pattern.txt"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def extract_verb_case_pattern():
    with open(OUTPUT_FILE_NAME, mode="w") as f:
        for chunks in load_nekocabocha_chunk():
            for chunk in chunks:
                if chunk.srcs == []:
                    continue
                if not chunk_include_pos(chunk, "動詞"):
                    continue
                if not chunk_include_pos(chunks[chunk.dst], "助詞"):
                    continue
                verb = extract_morph_from_chunk_by_pos(chunk, "動詞").base
                particles = " ".join([morph.base for morph in chunks[chunk.dst].morphs if morph.pos == "助詞"])
                f.write(f"{verb}\t{particles}\n")

# 1番左を抽出
def extract_morph_from_chunk_by_pos(chank, pos):
    for morph in chank.morphs:
        if morph.pos == pos:
            return morph
    return None

if __name__ == "__main__":
    extract_verb_case_pattern()
