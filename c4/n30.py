import os

FILE_NAME = "neko.txt.mecab"
CURRENT_DIR_NAME = os.path.dirname(__file__)

def load_mecab_text():
    import re
    pattern = r"^([^\t]+)\t([^,]+),([^,]+),[^,]+,[^,]+,[^,]+,[^,]+,([^,]+),[^,]*,[^,]*$"
    text = ""
    with open(os.path.join(CURRENT_DIR_NAME, FILE_NAME)) as f:
        text = f.read()
    # parse_results : [(表層形 (surface) : str, 品詞 (pos) : str, 品詞細分類1 (pos1) : str, 基本形 (base) : str)]
    parse_results = re.findall(pattern, text, re.MULTILINE)
    return [{"surface": line[0], "base": line[3], "pos": line[1], "pos1": line[2]} for line in parse_results]

if __name__ == "__main__":
    print(load_mecab_text()[0]["surface"])
