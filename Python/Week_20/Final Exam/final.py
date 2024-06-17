def main():
    words = []
    with open("dictionary.txt", 'r') as f:
        for line in f:
            words.append(line.strip().lower())
    words.sort()
    # print(words)

    sorted_words = {i: [] for i in range(3, 8)}
    for word in words:
        sorted_words[len(word)] += [word]


def superword(word: str):
    pass


def subword(word_a: str, word_b: str):
    # indexes = []
    # for letter in word_a:
    #     index = word_b.find(letter)
    #     if index == -1:
    #         return False
    #     if index in indexes:
    #         return False
    #     indexes.append(index)
    #     word_b = word_b[:index] + word_b[index+1:]
    # else:
    #     return True
    for letter in word_a:
        if word_a.count(letter) > word_b.count(letter):
            return False
    return True


print(subword("col", "workforce"))




if __name__ == '__main__':
    main()