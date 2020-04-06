import numpy as np
import matplotlib.pyplot as plt
from n30 import load_mecab_text
import math

def plot_zipfs_law():
    morphemes = load_mecab_text()
    frequency_of_morphemes = {}
    for morpheme in morphemes:
        frequency_of_morphemes[morpheme["base"]] = frequency_of_morphemes.setdefault(morpheme["base"], 0) + 1
    sorted_frequency_of_morphemes = sorted(frequency_of_morphemes.values(), reverse=True)

    x = [math.log10(i) for i in  np.arange(1, len(sorted_frequency_of_morphemes) + 1, 1)]
    y = [math.log10(i) for i in sorted_frequency_of_morphemes]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("両対数グラフ")
    ax.set_xlabel("単語の出現頻度順位(log10)")
    ax.set_ylabel("出現頻度(log10)")
    fig.savefig("n39.png")

if __name__ == "__main__":
    plot_zipfs_law()
