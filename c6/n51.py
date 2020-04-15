from sklearn.feature_extraction.text import TfidfVectorizer

docs: list = []
with open("train.txt") as f:
    docs = [line.strip().split("\t")[1] for line in f.readlines()]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)
print('feature_names:', vectorizer.get_feature_names())

words = vectorizer.get_feature_names()
print(len(words))
# for doc_id, vec in zip(range(len(docs)), X.toarray()):
#     print('doc_id:', doc_id)
#     for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True):
#         if tfidf == 0:
#             break
#         lemma = words[w_id]
#         print('\t{0:s}: {1:f}'.format(lemma, tfidf))
