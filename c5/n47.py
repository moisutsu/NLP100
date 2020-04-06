from n41 import load_nekocabocha_chunk
from n42 import chunk2str
from n43 import chunk_include_pos
from n45 import extract_morph_from_chunk_by_pos

OUTPUT_FILE_NAME = "functional_verb_constructions.txt"

def mining_functional_verb_constructions():
    with open(OUTPUT_FILE_NAME, mode="w") as f:
        for chunks in load_nekocabocha_chunk():
            for chunk in chunks:
                if len(chunk.morphs) != 2:
                    continue
                if chunk.srcs == []:
                    continue
                if not chunk.morphs[0].pos1 == "サ変接続":
                    continue
                if not chunk.morphs[1].base == "を":
                    continue
                if not chunk_include_pos(chunks[chunk.dst], "動詞"):
                    continue
                if not any([chunk_include_pos(chunks[i], "助詞") for i in chunk.srcs]):
                    continue
                noun = chunk2str(chunk)
                verb = extract_morph_from_chunk_by_pos(chunks[chunk.dst], "動詞").base
                particles = " ".join(morph.base for src_i in chunk.srcs for morph in chunks[src_i].morphs if morph.pos == "助詞")
                words = " ".join(chunk2str(chunks[i]) for i in chunk.srcs if chunk_include_pos(chunks[i], "助詞"))
                f.write(f"{noun}{verb}\t{particles}\t{words}\n")

def chunk_include_pos1(chunk, pos1) -> bool:
    return any([morph.pos1 == pos1 for morph in chunk.morphs])

if __name__ == "__main__":
    mining_functional_verb_constructions()
