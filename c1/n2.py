def concat_string(arg1: str, arg2: str) -> str:
    return "".join(a + b for a, b in zip(arg1, arg2))

if __name__ == "__main__":
    print(concat_string("パトカー", "タクシー"))
