import gensim
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format("word_vec.bin", binary=True)

calc_vec = model["Spain"] - model["Madrid"] + model["Athens"]
results = model.most_similar([calc_vec], [], 10)
for result in results:
    print(result)
