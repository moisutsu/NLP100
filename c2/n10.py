import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def wc(file_name: str) -> int:
    with open(file_name) as f:
        return len(f.readlines())

if __name__ == "__main__":
    print(wc(INPUT_FILE_NAME))
