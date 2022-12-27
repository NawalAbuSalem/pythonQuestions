import re


def get_word_format(string):
    word = re.search(r'\b\w+\b', string).group()
    return word + ":" + word + "." + word


print(get_word_format("number one is the first"))
