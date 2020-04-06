from n41 import load_nekocabocha_chunk
from n42 import chunk2str
from n43 import chunk_include_pos

def extract_dependency_path():
    for chunks in load_nekocabocha_chunk():
        for chunk in chunks:
            if not chunk_include_pos(chunk, "名詞"):
                continue
            if chunk.dst == -1:
                continue
            path_to_root = chunk2str(chunk)
            while chunk.dst != -1:
                chunk = chunks[chunk.dst]
                path_to_root += f" -> {chunk2str(chunk)}"
            print(path_to_root)

if __name__ == "__main__":
    extract_dependency_path()
