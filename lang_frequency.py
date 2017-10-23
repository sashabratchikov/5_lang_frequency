import collections
from sys import argv

NUMBER_OF_WORDS = 10


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    return list(map(lambda item: item[0],
                collections.Counter(text.split())
                .most_common(NUMBER_OF_WORDS)))


if __name__ == '__main__':
    text = load_data(argv[1])
    print(get_most_frequent_words(text))
