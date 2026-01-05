import string

if __name__ == '__main__':
    txt = "The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the English alphabet"
    length_of_words = [len(word.strip(string.punctuation)) for word in txt.lower().split() if word.strip(string.punctuation) != "the"]
    print(length_of_words)

    #zad6
    three_d = [
        [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
        [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
    ]

    res = []
    for sublist in three_d:
        for subsublist in sublist:
            if len(subsublist) > 4:
                res.append(subsublist)

    print(res)