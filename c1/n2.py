def n2(arg1, arg2):
    return "".join([a + b for a, b in zip(arg1, arg2)])

if __name__ == "__main__":
    print(n2("パトカー", "タクシー"))
