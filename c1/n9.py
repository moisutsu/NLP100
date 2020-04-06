def typoglycemia(sentence: str) -> str:
    import random
    return " ".join(f"{word[0]}{''.join(random.sample(word[1:-1], k=len(word) - 2))}{word[-1]}" if len(word) > 4 else word for word in sentence.split())

if __name__ == "__main__":
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(typoglycemia(sentence))
