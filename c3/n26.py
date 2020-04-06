from n20 import load_england_text
from n25 import extract_basic_information_as_dict

def remove_emphasis_markup(text: str) -> str:
    return text.replace("'", "")

def remove_dict_emphasis_markup(dic: dict) -> dict:
    for key in dic.keys():
        dic[key] = remove_emphasis_markup(dic[key])
    return dic

if __name__ == "__main__":
    text = load_england_text()
    basic_info_dict = extract_basic_information_as_dict(text)
    basic_info_dict = remove_dict_emphasis_markup(basic_info_dict)
    [print(f"{key}: {value}") for key, value in basic_info_dict.items()]
