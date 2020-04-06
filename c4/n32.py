from n30 import load_mecab_text

def extract_verbs_base():
    morphemes = load_mecab_text()
    return [morpheme["base"] for morpheme in morphemes if morpheme["pos"] == "動詞"]

if __name__ == "__main__":
    print(*extract_verbs_base(), sep=" ")
