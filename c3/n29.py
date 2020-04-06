from n20 import load_england_text
from n25 import extract_basic_information_as_dict
from n26 import remove_dict_emphasis_markup
from n27 import remove_dict_internal_link
from n28 import remove_dict_mediawiki_markup
import regex
import requests
import json

API_URL = "https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles=File%3A{}"
FLAG_URL = "https://ja.wikipedia.org/wiki/イギリス#/media/{}"

def get_shaped_basic_information_as_dict(text: str) -> dict:
    basic_info_dict = extract_basic_information_as_dict(text)
    basic_info_dict = remove_dict_emphasis_markup(basic_info_dict)
    basic_info_dict = remove_dict_internal_link(basic_info_dict)
    basic_info_dict = remove_dict_mediawiki_markup(basic_info_dict)
    return basic_info_dict

def fetch_national_flag_image_url(dic: dict) -> str:
    url = API_URL.format(dic["国旗画像"])
    response = requests.get(url)
    json_body = response.json()
    return FLAG_URL.format(json_body["query"]["normalized"][0]["to"])

if __name__ == "__main__":
    text = load_england_text()
    basic_info_dict = get_shaped_basic_information_as_dict(text)
    print(fetch_national_flag_image_url(basic_info_dict))
