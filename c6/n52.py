from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

def load_datas(file_name: str) -> tuple:
    docs: np.ndarray = []
    with open(file_name) as f:
        docs = np.array([line.strip().split("\t") for line in f.readlines()])
    X = docs[:, 1]
    Y = docs[:, 0]
    return X, Y

if __name__ == "__main__":
    vectorizer = TfidfVectorizer()
    X_train, Y_train = load_datas("train.txt")
    X_train = vectorizer.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # X_test, Y_test = load_datas("test.txt")
    # X_test = vectorizer.transform(X_test)
    # test_result = model.predict(X_test)
    # print(accuracy_score(test_result, Y_test))
