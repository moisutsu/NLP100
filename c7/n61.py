import gensim
import numpy as np

model = gensim.models.KeyedVectors.load_word2vec_format("word_vec.bin", binary=True)

model["United_States"] @ model["U.S."] / (np.linalg.norm(model["United_States"], ord=2) * np.linalg.norm(model["U.S."], ord=2))
