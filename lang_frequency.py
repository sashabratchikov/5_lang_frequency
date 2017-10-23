from sys import argv


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    words_list = text.split()
    frequencies = {}
    for word in words_list:
        if frequencies.get(word):
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1
    frequencies_list = list(frequencies.items())
    frequencies_list.sort(key=lambda item: -item[1])
    return list(map(lambda item: item[0], frequencies_list[:10]))


if __name__ == '__main__':
    text = load_data(argv[1])
    print(get_most_frequent_words(text))
