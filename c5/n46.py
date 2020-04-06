from n41 import load_nekocabocha_chunk
from n42 import chunk2str
from n43 import chunk_include_pos
from n45 import extract_morph_from_chunk_by_pos

def extract_verb_case_frames():
    for chunks in load_nekocabocha_chunk():
        for chunk in chunks:
            if chunk.srcs == []:
                continue
            if not chunk_include_pos(chunk, "動詞"):
                continue
            if not any([chunk_include_pos(chunks[i], "助詞") for i in chunk.srcs]):
                continue
            verb = extract_morph_from_chunk_by_pos(chunk, "動詞").base
            particles = " ".join(morph.base for src_i in chunk.srcs for morph in chunks[src_i].morphs if morph.pos == "助詞")
            words = " ".join(chunk2str(chunks[i]) for i in chunk.srcs if chunk_include_pos(chunks[i], "助詞"))
            print(f"{verb}\t{particles}\t{words}")

if __name__ == "__main__":
    extract_verb_case_frames()
