from dataclasses import dataclass
import os
from n40 import load_nekocabocha_sentences, Morph

os.chdir(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class Chunk:
    morphs: list
    dst: int
    srcs: list

# 文節リストを返すジェネレータ
def load_nekocabocha_chunk():
    sentences = load_nekocabocha_sentences()

    import re
    morph_pattern = r"^([^\t\n]+)\t([^,]+),([^,]+),[^,]+,[^,]+,[^,]+,[^,]+,([^,]+),[^,]*,[^,]*$"
    dependency_pattern = r"^\*\s\d+\s(-?\d+)D\s-?\d+/-?\d+\s[-\d\.]+$"

    for sentence in sentences:
        chunks = []
        if sentence == "EOS":
            yield chunks
            continue

        for line in sentence.split("\n"):
            if dependency_result := re.match(dependency_pattern, line):
                # 文節の係り先文節インデックスを先にリストに追加
                chunks.append(Chunk(morphs = [], dst=int(dependency_result.group(1)), srcs = []))
            elif morph_result := re.match(morph_pattern, line):
                morph = Morph(surface = morph_result.group(1), base = morph_result.group(4), pos = morph_result.group(2), pos1 = morph_result.group(3))
                chunks[-1].morphs.append(morph)
            else:
                pass

        # 係り元文節インデックスを設定
        for i, chunk in enumerate(chunks):
            if chunk.dst != -1:
                chunks[chunk.dst].srcs.append(i)
        yield chunks


if __name__ == "__main__":
    print(*list(load_nekocabocha_chunk())[7], sep="\n")
