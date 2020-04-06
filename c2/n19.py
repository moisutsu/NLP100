import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def col1_freq(file_name: str) -> list:
    word_freq = {}
    with open(file_name) as f:
        columns = [line.strip().split()[0] for line in f.readlines()]
        for column in columns:
            word_freq[column] = word_freq.setdefault(column, 0) + 1
    return sorted(word_freq.items(), reverse=True, key=lambda x: x[1])

if __name__ == "__main__":
    print(*col1_freq(INPUT_FILE_NAME), sep="\n")
