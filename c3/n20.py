import json
import os

FILE_NAME = "jawiki-country.json"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def load_england_text():
    with open(absolute_path) as f:
        lines = f.readlines()
        for line in lines:
            json_body = json.loads(line)
            if json_body["title"] == "イギリス":
                return json_body["text"]

if __name__ == "__main__":
    print(load_england_text())
