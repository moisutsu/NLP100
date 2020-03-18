import os

os.chdir(os.path.dirname(__file__))

def head(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        print("".join(lines[:N - len(lines)]))

if __name__ == "__main__":
    N = int(input("N: "))
    head("hightemp.txt", N)
