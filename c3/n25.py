from n20 import load_england_text
import regex

def extract_basic_information_as_dict(text: str) -> dict:
    # 再帰的に{{}}で囲まれた箇所を抽出
    rec_pattern = r"(?<recursive_brackets>\{\{(?:[^{}]+|(?&recursive_brackets))*\}\})"
    # {{}}で囲まれた箇所のうち,"基礎情報"が含まれた文字列を抽出
    basic_information_result = [result for result in regex.findall(rec_pattern, text) if "基礎情報" in result][0]
    remove_outside_brackets_result = regex.sub(r"(?:^.*|}}$)", "", basic_information_result)
    remove_extra_indent_resfult = regex.sub(r"\n[^\|]", "", remove_outside_brackets_result)
    eq_pattern = r"^\|([^\s]*)\s=\s(.*)$"
    results = regex.findall(eq_pattern, remove_extra_indent_resfult, regex.MULTILINE)
    return {elem[0]: elem[1] for elem in results}

if __name__ == "__main__":
    text = load_england_text()
    basic_info = extract_basic_information_as_dict(text)
    [print(f"{key}: {value}") for key, value in basic_info.items()]
