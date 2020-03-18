import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def head(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        print("".join(lines[:N - len(lines)]))

if __name__ == "__main__":
    N = int(input("N: "))
    head(absolute_path, N)
