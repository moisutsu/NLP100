import pydot
from dataclasses import dataclass
import os
from n41 import load_nekocabocha_chunk
from n42 import chunk2str

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def save_tree_img(index: int):
    chunks = list(load_nekocabocha_chunk())[index]
    edges = []
    for i, chunk in enumerate(chunks):
        if chunk.dst == -1:
            continue
        edges.append(((i, chunk2str(chunk)), (chunk.dst, chunk2str(chunks[chunk.dst]))))
    g = pydot.graph_from_edges(edges)
    g.write_jpeg('graph_from_edges_dot.jpg', prog='dot')


if __name__ == "__main__":
    save_tree_img(7)
