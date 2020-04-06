import numpy as np
import matplotlib.pyplot as plt
from n30 import load_mecab_text

def plot_histogram_frequency_of_morphemes():
    morphemes = load_mecab_text()
    frequency_of_morphemes = {}
    for morpheme in morphemes:
        frequency_of_morphemes[morpheme["base"]] = frequency_of_morphemes.setdefault(morpheme["base"], 0) + 1
    sorted_frequency_of_morphemes = sorted(frequency_of_morphemes.values(), reverse=True)

    fig, ax = plt.subplots()
    ax.hist(sorted_frequency_of_morphemes, bins=100, range=(0, 1000))
    ax.set_title("ヒストグラム")
    ax.set_xlabel("出現頻度")
    ax.set_ylabel("出現頻度をとる単語の種類数")
    fig.savefig("n38.png")

if __name__ == "__main__":
    plot_histogram_frequency_of_morphemes()
