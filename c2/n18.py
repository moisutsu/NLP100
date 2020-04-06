import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "popular-names.txt"

def col3_sort(file_name: str) -> list:
    with open(file_name) as f:
        lines = [line.strip().split() for line in f.readlines()]
        lines.sort(reverse=True, key=lambda x: int(x[2]))
        # リストのりストから文字列のリストへ変換
        return ["\t".join(line) for line in lines]

if __name__ == "__main__":
    print(*col3_sort(INPUT_FILE_NAME), sep="\n")
