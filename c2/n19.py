import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def col1_freq(file_name):
    word_freq = {}
    with open(file_name) as f:
        columns = [line.strip().split()[0] for line in f.readlines()]
        for column in columns:
            word_freq[column] = word_freq.setdefault(column, 0) + 1
    return sorted(word_freq.items(), reverse=True, key=lambda x: x[1])

if __name__ == "__main__":
    print(*col1_freq(absolute_path), sep="\n")
