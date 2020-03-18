import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def uniq(file_name):
    with open(file_name) as f:
        return set(line.strip().split()[0] for line in f.readlines())

if __name__ == "__main__":
    print(uniq(absolute_path))
