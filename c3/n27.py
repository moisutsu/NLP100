from n20 import load_england_text
from n25 import extract_basic_information_as_dict
from n26 import remove_dict_emphasis_markup
import regex

def remove_internal_link(text: str) -> str:
    pattern = r"\[\[(?:[^\|\[\]]+\|)?([^\[\]]*)\]\]"
    return regex.sub(pattern, r"\1", text)

def remove_dict_internal_link(dic: dict) -> dict:
    for key in dic.keys():
        dic[key] = remove_internal_link(dic[key])
    return dic

if __name__ == "__main__":
    text = load_england_text()
    basic_info_dict = extract_basic_information_as_dict(text)
    basic_info_dict = remove_dict_emphasis_markup(basic_info_dict)
    basic_info_dict = remove_dict_internal_link(basic_info_dict)
    [print(f"{key}: {value}") for key, value in basic_info_dict.items()]
