from n20 import load_england_text
import regex

def n26():
    text = load_england_text()
    rec_pattern = r"(?<recursive_brackets>\{\{(?:[^{}]+|(?&recursive_brackets))*\}\})"
    basic_information_result = regex.findall(rec_pattern, text)[1]
    remove_outside_brackets_result = regex.sub(r"(?:^.*|}}$)", "", basic_information_result)
    remove_extra_indent_resfult = regex.sub(r"\n[^\|]", "", remove_outside_brackets_result)
    eq_pattern = r"^\|([^\s]*)\s=\s(.*)$"
    results = regex.findall(eq_pattern, remove_extra_indent_resfult, regex.MULTILINE)
    return {elem[0]: elem[1] for elem in results}

if __name__ == "__main__":
    print(*n26().items(), sep="\n")
