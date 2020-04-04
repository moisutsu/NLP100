import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"
OUTPUT_FILE_NAME_1 = "cut1.txt"
OUTPUT_FILE_NAME_2 = "cut2.txt"

def cut(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        cells1, cells2 = [line.split("\t")[0] for line in lines], [line.split("\t")[1] for line in lines]
        with open(OUTPUT_FILE_NAME_1, mode="w") as f1:
            f1.write("\n".join(cells1))
        with open(OUTPUT_FILE_NAME_2, mode="w") as f2:
            f2.write("\n".join(cells2))


if __name__ == "__main__":
    cut(INPUT_FILE_NAME)
