def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    totalWords = wordCount(file_contents)
    totalLetters = letterCount(file_contents)
    ("the total number of words in this book is", totalWords)
    print("the total number of times each letter appears in this book is:", totalLetters)


def wordCount(string):
    total = string.split()
    count = 0
    for i in total:
        count += 1
    return count


def letterCount(string):
    lowerCase = string.lower()
    letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, ' m': 0,
               'n': 0, 'o': 0, ' p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    characters = {}
    for i in lowerCase:
        for j in characters.keys():
            if i == j:
                letters[j] += 1
    return letters


if __name__ == '__main__':
    main()
