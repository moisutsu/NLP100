import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def head(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        print("".join(lines[:N - len(lines)]))

if __name__ == "__main__":
    head(INPUT_FILE_NAME, int(sys.argv[1]))
