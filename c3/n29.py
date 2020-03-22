from n20 import load_england_text
import regex
import requests
import json

API_URL = "https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&titles=File%3A{}"
FLAG_URL = "https://ja.wikipedia.org/wiki/イギリス#/media/{}"

def n29():
    text = load_england_text()
    rec_pattern = r"(?<recursive_brackets>\{\{(?:[^{}]+|(?&recursive_brackets))*\}\})"
    basic_information_result = regex.findall(rec_pattern, text)[1]
    remove_outside_brackets_result = regex.sub(r"(?:^.*|}}$)", "", basic_information_result)
    remove_extra_indent_resfult = regex.sub(r"\n[^\|]", "", remove_outside_brackets_result)
    remove_internal_links_result = regex.sub(r"\[\[(?:[^\|\[\]]+\|)?([^\[\]]*)\]\]", r"\1", remove_extra_indent_resfult)
    remove_mediawiki_markup_result = regex.sub(r"<br\s?/>|<ref[^/>]*/?>|</ref>", "", remove_internal_links_result)
    eq_pattern = r"^\|([^\s]*)\s=\s(.*)$"
    results = regex.findall(eq_pattern, remove_mediawiki_markup_result, regex.MULTILINE)
    results_dic = {elem[0]: elem[1] for elem in results}
    url = API_URL.format(results_dic["国旗画像"])
    response = requests.get(url)
    json_body = response.json()
    print(FLAG_URL.format(json_body["query"]["normalized"][0]["to"]))

if __name__ == "__main__":
    n29()
