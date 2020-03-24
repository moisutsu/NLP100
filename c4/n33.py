from n30 import load_mecab_text

def n33():
    morphemes = load_mecab_text()
    return [morpheme["base"] for morpheme in morphemes if morpheme["pos"] == "名詞" and morpheme["pos1"] == "サ変接続"]

if __name__ == "__main__":
    print(*n33(), sep=" ")
