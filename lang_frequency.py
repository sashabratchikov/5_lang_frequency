from sys import argv
import collections


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def get_most_frequent_words(text, number_of_words=10):
    return [word[0] for word in collections.Counter(text.split())
                                           .most_common(number_of_words)]


if __name__ == '__main__':
    text = load_data(argv[1])
    print('Ten most frequent words: ', get_most_frequent_words(text))
