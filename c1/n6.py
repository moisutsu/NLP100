def bi_gram(sequence):
    sentence = sequence.replace(" ", "")
    return [sentence[i] + sentence[i + 1] for i in range(len(sentence) - 1)]

if __name__ == "__main__":
    X = set(bi_gram("paraparaparadise"))
    Y = set(bi_gram("paragraph"))
    print(f"X: {X}")
    print(f"Y: {Y}")
    print(f"X | Y: {X | Y}")
    print(f"X - Y: {X - Y}")
    print(f"X & Y: {X & Y}")
    if "se" in X:
        print('"se" in X')
    if "se" in Y:
        print('"se" in Y')
