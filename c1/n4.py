def n4(sentence, indexs):
    import re
    pattern = r"[a-zA-Z]+"
    results = re.findall(pattern, sentence)
    keys = [results[i][0] if i + 1 in indexs else results[i][:2] for i in range(len(results))]
    return {key: value for key, value in zip(keys, list(range(1, len(results) + 1)))}

if __name__ == "__main__":
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    indexs = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    print(n4(sentence, indexs))
