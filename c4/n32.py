from n30 import load_mecab_text

def n32():
    morphemes = load_mecab_text()
    return [morpheme["base"] for morpheme in morphemes if morpheme["pos"] == "動詞"]

if __name__ == "__main__":
    print(*n32(), sep=" ")
