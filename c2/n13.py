import os

os.chdir(os.path.dirname(__file__))

def paste(file_name_1, file_name_2):
    col1, col2 = [], []
    with open(file_name_1) as f:
        col1.extend([line.strip() for line in f.readlines()])
    with open(file_name_2) as f:
        col2.extend([line.strip() for line in f.readlines()])
    with open("merge.txt", mode="w") as f:
        f.write("\n".join(f"{cell1}\t{cell2}" for cell1, cell2 in zip(col1, col2)))

if __name__ == "__main__":
    paste("col1.txt", "col2.txt")
