from n30 import load_mecab_text

def n36():
    morphemes = load_mecab_text()
    frequency_of_morphemes = {}
    for morpheme in morphemes:
        frequency_of_morphemes[morpheme["base"]] = frequency_of_morphemes.setdefault(morpheme["base"], 0) + 1
    return [line[0] for line in sorted(frequency_of_morphemes.items(), key=lambda x: x[1], reverse=True)]

if __name__ == "__main__":
    print(*n36())
