def cipher(sentence: str) -> str:
    return "".join(chr(219 - ord(c)) if c.islower() else c for c in sentence)


if __name__ == "__main__":
    sentence = "I am writing Python program."
    print(cipher(sentence))
    print(cipher(cipher(sentence)))
