import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def cut(file_name):
    col1_file_name = os.path.join(os.path.dirname(__file__), "col1.txt")
    col2_file_name = os.path.join(os.path.dirname(__file__), "col2.txt")
    with open(file_name) as f:
        lines = f.readlines()
        cells1, cells2 = [line.split()[0] for line in lines], [line.split()[1] for line in lines]
        with open(col1_file_name, mode="w") as f1:
            f1.write("\n".join(cells1))
        with open(col2_file_name, mode="w") as f2:
            f2.write("\n".join(cells2))


if __name__ == "__main__":
    cut(absolute_path)
