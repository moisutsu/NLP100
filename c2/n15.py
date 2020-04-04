import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def tail(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        print("".join(lines[len(lines) - N:]))

if __name__ == "__main__":
    tail(INPUT_FILE_NAME, int(sys.argv[1]))
