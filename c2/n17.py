import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def uniq(file_name):
    with open(file_name) as f:
        print(*set(line.strip().split("\t")[0] for line in f.readlines()), sep="\n")

if __name__ == "__main__":
    uniq(INPUT_FILE_NAME)
