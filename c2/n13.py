import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME_1 = "cut1.txt"
INPUT_FILE_NAME_2 = "cut2.txt"
OUTPUT_FILE_NAME = "merge.txt"

def paste(file_name_1: str, file_name_2: str) -> None:
    col1, col2 = [], []
    with open(file_name_1) as f:
        col1.extend([line.strip() for line in f.readlines()])
    with open(file_name_2) as f:
        col2.extend([line.strip() for line in f.readlines()])
    with open(OUTPUT_FILE_NAME, mode="w") as f:
        f.write("\n".join(f"{cell1}\t{cell2}" for cell1, cell2 in zip(col1, col2)))

if __name__ == "__main__":
    paste(INPUT_FILE_NAME_1, INPUT_FILE_NAME_2)
