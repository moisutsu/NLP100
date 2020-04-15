import gensim

model = gensim.models.KeyedVectors.load_word2vec_format("word_vec.bin", binary=True)

print(model["United_States"])
