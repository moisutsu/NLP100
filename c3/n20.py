import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE_NAME = "jawiki-country.json"

def load_england_text() -> str:
    with open(INPUT_FILE_NAME) as f:
        lines = f.readlines()
        for line in lines:
            json_body = json.loads(line)
            if json_body["title"] == "イギリス":
                return json_body["text"]

if __name__ == "__main__":
    print(load_england_text())
