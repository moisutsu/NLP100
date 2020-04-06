from n30 import load_mecab_text

def extract_nouns_a_no_b():
    morphemes = load_mecab_text()
    return [f"{morphemes[i]['surface']}の{morphemes[i + 2]['surface']}" for i in range(len(morphemes) - 2) if morphemes[i]["pos"] == "名詞" and morphemes[i + 1]["surface"] == "の" and morphemes[i + 2]["pos"] == "名詞"]

if __name__ == "__main__":
    print(*extract_nouns_a_no_b(), sep=" ")
