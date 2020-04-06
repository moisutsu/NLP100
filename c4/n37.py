import numpy as np
import matplotlib.pyplot as plt
from n30 import load_mecab_text

def plot_co_occurrence_frequency_with_neko():
    morphemes = load_mecab_text()

    # 「。」が来るまでの単語を格納し,その中に「猫」が含まれていたらco_occurrence_morphemesに追加
    co_occurrence_words = []
    tmp_words = []
    for morpheme in morphemes:
        if morpheme["base"] == "。":
            if "猫" in tmp_words:
                co_occurrence_words.extend([elem for elem in tmp_words if elem != "猫"])
            tmp_words = []
            continue
        tmp_words.append(morpheme["base"])

    frequency_of_words = {}
    for word in co_occurrence_words:
        frequency_of_words[word] = frequency_of_words.setdefault(word, 0) + 1
    sorted_frequency_of_words = [(line[0], line[1]) for line in sorted(frequency_of_words.items(), key=lambda x: x[1], reverse=True)][:10]

    x = np.arange(len(sorted_frequency_of_words))
    labels = [line[0] for line in sorted_frequency_of_words]
    means = [line[1] for line in sorted_frequency_of_words]
    fig, ax = plt.subplots()
    ax.bar(x, means)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title("「猫」と共起頻度の高い上位10語")
    ax.set_xlabel("単語")
    ax.set_ylabel("共起頻度")
    fig.savefig("n37.png")

if __name__ == "__main__":
    plot_co_occurrence_frequency_with_neko()
