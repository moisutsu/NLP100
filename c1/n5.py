def n5_word(sequence):
    import re
    pattern = r"[a-zA-Z]+"
    results = re.findall(pattern, sequence)
    return bi_gram(results)

def n5_char(sequence):
    return bi_gram(sequence.replace(" ", ""))

def bi_gram(sequence):
    return [sequence[i] + sequence[i + 1] for i in range(len(sequence) - 1)]

if __name__ == "__main__":
    sequence = "I am an NLPer"
    print(n5_word(sequence))
    print(n5_char(sequence))
