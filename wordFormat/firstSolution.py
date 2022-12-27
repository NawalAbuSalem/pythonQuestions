
def get_word_format(string):
    words = string.split(" ")
    return words[0] + ":" + words[0] + "." + words[0]


print(get_word_format("number one is the first"))
