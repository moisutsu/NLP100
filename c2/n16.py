import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def split(file_name, N):
    file_contents = []
    with open(file_name) as f:
        lines = [line.strip() for line in f.readlines()]
        file_contents.extend([lines[i:i+N] for i in range(0, len(lines), N)])
    for i, file_content in enumerate(file_contents):
        with open(f"split{i}.txt", mode="w") as f:
            f.write("\n".join(file_content))

if __name__ == "__main__":
    N = int(input("N: "))
    split(absolute_path, N)
