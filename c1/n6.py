def n_gram(sequence, n):
    return ["".join(sequence[i:i + n]) for i in range(len(sequence) - n + 1)]

if __name__ == "__main__":
    X = set(n_gram("paraparaparadise", 2))
    Y = set(n_gram("paragraph", 2))
    print(f"X: {X}")
    print(f"Y: {Y}")
    print(f"X | Y: {X | Y}")
    print(f"X - Y: {X - Y}")
    print(f"X & Y: {X & Y}")
    "se" in X and print('"se" in X')
    "se" in Y and print('"se" in Y')
