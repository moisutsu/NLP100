from n20 import load_england_text
from n25 import extract_basic_information_as_dict
from n26 import remove_dict_emphasis_markup
from n27 import remove_dict_internal_link
import regex

def remove_mediawiki_markup(text: str) -> str:
    # br, ref を削除
    br_pattern = r"<br\s?/>"
    ref_pattern = r"<ref[^/>]*/?>|</ref>"
    text = regex.sub(br_pattern, "", text)
    text = regex.sub(ref_pattern, "", text)

    # {{lang| | }}のパターンを削除
    lang_pattern = r"{{lang\|[^|]*\|([^}]+)}}"
    text = regex.sub(lang_pattern, r"\1", text)

    # 仮リンクパターンを削除
    temporary_link_pattern = r"{{仮リンク\|([^|]+).*?}}"
    text = regex.sub(temporary_link_pattern, r"\1", text)

    # 残りの{{}}パターンを削除
    double_braces_pattern = r"{{[^}]+}}"
    text = regex.sub(double_braces_pattern, "", text)

    # []パターンを削除
    square_brackets = r"\[[^]]*\]"
    text = regex.sub(square_brackets, "", text)

    return text

def remove_dict_mediawiki_markup(dic: dict) -> dict:
    for key in dic.keys():
        dic[key] = remove_mediawiki_markup(dic[key])
    return dic

if __name__ == "__main__":
    text = load_england_text()
    basic_info_dict = extract_basic_information_as_dict(text)
    basic_info_dict = remove_dict_emphasis_markup(basic_info_dict)
    basic_info_dict = remove_dict_internal_link(basic_info_dict)
    basic_info_dict = remove_dict_mediawiki_markup(basic_info_dict)
    [print(f"{key}: {value}") for key, value in basic_info_dict.items()]
