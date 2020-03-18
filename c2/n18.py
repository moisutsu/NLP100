import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def col3_sort(file_name):
    with open(file_name) as f:
        lines = [line.strip().split() for line in f.readlines()]
        lines.sort(reverse=True, key=lambda x: float(x[2]))
        return lines

if __name__ == "__main__":
    print(*col3_sort(absolute_path), sep="\n")
