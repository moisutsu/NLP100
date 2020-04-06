import numpy as np
import matplotlib.pyplot as plt
from n30 import load_mecab_text
from n35 import sorted_frequency_of_morphemes

def plot_frequency_of_morphemes_top10():
    sorted_morphemes = sorted_frequency_of_morphemes()[:10]
    x = np.arange(len(sorted_morphemes))
    labels = [line[0] for line in sorted_morphemes]
    means = [line[1] for line in sorted_morphemes]
    fig, ax = plt.subplots()
    ax.bar(x, means)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_title("頻度上位10語")
    ax.set_xlabel("単語")
    ax.set_ylabel("出現頻度")
    fig.savefig("n36.png")

if __name__ == "__main__":
    plot_frequency_of_morphemes_top10()
