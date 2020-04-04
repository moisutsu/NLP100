import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def tr(file_name):
    with open(file_name) as f:
        return f.read().replace("\t", " ")

if __name__ == "__main__":
    print(tr(INPUT_FILE_NAME))
