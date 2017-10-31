import sys
import collections


def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return text_file.read()


def get_most_frequent_words(text, number_of_words=10):
    WordFrequency = collections.namedtuple('WordFrequency',
                                           ['word', 'frequency'])
    return [WordFrequency(*entity).word for entity in collections
            .Counter(text.split())
            .most_common(number_of_words)]


if __name__ == '__main__':
    file_path = None
    try:
        file_path = sys.argv[1]
        text = load_data(file_path)
    except IndexError:
        print('Enter path to file: python pprint_json.py <path to file>')
        sys.exit(1)
    except FileNotFoundError:
        print('File you provided: {} not found'.format(file_path))
        sys.exit(1)
    print('Ten most frequent words from {} in descending order: '
          .format(file_path),
          get_most_frequent_words(text))
