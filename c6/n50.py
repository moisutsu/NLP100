import csv
import os
from random import shuffle
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def make_dataset():
    publishers = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]

    extracted_articles: list = []
    with open("NewsAggregatorDataset/newsCorpora.csv") as f:
        reader = csv.reader(f, delimiter="\t")
        extracted_articles = [[article[4], article[1]] for article in reader if article[3] in publishers]
    shuffle(extracted_articles)

    # 文書の前処理を行う
    # https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F309361%2F503898e6-b031-7840-7da8-6d7d3d6c5c8f.png?ixlib=rb-1.2.2&auto=format&gif-q=60&q=75&s=bec94fa51932f9fa459b384a3a76d0b8
    # クリーニング処理
    extracted_articles = [[line[0],
    re.sub(r"[^\w\s]", "", line[1])
    ]for line in extracted_articles]
    # 単語の正規化
    extracted_articles = [[line[0],
    line[1].lower()
    ]for line in extracted_articles]
    # ステミング処理
    snowball = SnowballStemmer(language="english")
    extracted_articles = [[line[0],
    " ".join([snowball.stem(word) for word in line[1].split()])
    ]for line in extracted_articles]
    # 数値を0に変換する
    extracted_articles = [[line[0],
    re.sub(r"\d+", "0", line[1])
    ] for line in extracted_articles]
    # ストップワードを除去
    stop_words = stopwords.words("english")
    extracted_articles = [[line[0],
    " ".join([word for word in line[1].split() if not word in stop_words])
    ]for line in extracted_articles]

    length_unit = int(len(extracted_articles) / 10)
    with open("train.txt", mode="w") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(extracted_articles[:length_unit * 8])

    with open("valid.txt", mode="w") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(extracted_articles[length_unit * 8:length_unit * 9])

    with open("test.txt", mode="w") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(extracted_articles[length_unit * 9:])

if __name__ == "__main__":
    make_dataset()
    with open("train.txt") as f:
        print(f"train.txt: {len(f.readlines())} lines")
    with open("valid.txt") as f:
        print(f"valid.txt: {len(f.readlines())} lines")
    with open("test.txt") as f:
        print(f"test.txt: {len(f.readlines())} lines")
