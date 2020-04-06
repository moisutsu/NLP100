def n_gram(sequence, n: int) -> list:
    return ["".join(sequence[i:i + n]) for i in range(len(sequence) - n + 1)]

if __name__ == "__main__":
    sequence = "I am an NLPer"
    print(n_gram(sequence, 2))
    print(n_gram(sequence.split(), 3))
