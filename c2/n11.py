import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def tr(file_name):
    with open(file_name) as f:
        for line in f.readlines():
            print(line.replace("\t", " "), end="")

if __name__ == "__main__":
    tr(absolute_path)
