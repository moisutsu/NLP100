import numpy as np
import matplotlib.pyplot as plt
from n30 import load_mecab_text

def n37():
    morphemes = load_mecab_text()
    frequency_of_morphemes = {}
    for morpheme in morphemes:
        frequency_of_morphemes[morpheme["base"]] = frequency_of_morphemes.setdefault(morpheme["base"], 0) + 1
    sorted_frequency_of_morphemes = sorted(frequency_of_morphemes.items(), key=lambda x: x[1], reverse=True)[:10]

    x = np.arange(len(sorted_frequency_of_morphemes))
    labels = [line[0] for line in sorted_frequency_of_morphemes]
    means = [line[1] for line in sorted_frequency_of_morphemes]
    fig, ax = plt.subplots()
    ax.bar(x, means)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title("頻度上位10語")
    ax.set_xlabel("単語")
    ax.set_ylabel("出現頻度")
    fig.savefig("n37.png")


if __name__ == "__main__":
    n37()
