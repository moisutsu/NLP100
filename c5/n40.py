from dataclasses import dataclass
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

@dataclass(frozen=True)
class Morph:
    surface: str
    base: str
    pos: str
    pos1: str

def load_nekocabocha_sentences():
    file_text = ""
    with open("neko.txt.cabocha") as f:
        file_text = f.read().replace("EOS", "EOS\n")

    # ファイルを空行で区切り(1文章ごと)、リストにして返す
    return [block.strip() for block in file_text.split("\n\n")]

# 二次リストを返す
# 要素は文章ごとの形態素のリスト
def analysis_nekocabocha_text():
    import re
    pattern = r"^([^\t\n]+)\t([^,]+),([^,]+),[^,]+,[^,]+,[^,]+,[^,]+,([^,]+),[^,]*,[^,]*$"

    retval = []
    sentences = load_nekocabocha_sentences()
    for sentence in sentences:
        if sentence == "EOS":
            continue
        # parse_results : [(表層形 (surface): str, 品詞 (pos): str, 品詞細分類1 (pos1): str, 基本形 (base): str)]
        parse_results = re.findall(pattern, sentence, re.MULTILINE)
        retval.append([line2morph(line) for line in parse_results])
    return retval

def line2morph(line) -> Morph:
    return Morph(surface = line[0], base = line[3], pos = line[1], pos1 = line[2])

if __name__ == "__main__":
    print(analysis_nekocabocha_text()[2])
