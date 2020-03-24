from n30 import load_mecab_text

def n35():
    morphemes = load_mecab_text()
    longest_nouns = []
    joined_noun = ""
    for morpheme in morphemes:
        if morpheme["pos"] == "名詞":
            joined_noun += morpheme["surface"]
        elif joined_noun != "":
            longest_nouns.append(joined_noun)
            joined_noun = ""
    return longest_nouns


if __name__ == "__main__":
    print(*n35(), sep=" ")
