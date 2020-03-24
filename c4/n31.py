from n30 import load_mecab_text

def n31():
    morphemes = load_mecab_text()
    return [morpheme["surface"] for morpheme in morphemes if morpheme["pos"] == "動詞"]

if __name__ == "__main__":
    print(*n31(), sep=" ")
