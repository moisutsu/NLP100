import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def wc(file_name):
    with open(file_name) as f:
        return len(f.readlines())

if __name__ == "__main__":
    print(wc(absolute_path))
