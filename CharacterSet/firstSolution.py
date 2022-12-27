
def get_char_set(string):
    character_set = []
    for index in range(len(string)):
        character_set.append(string[index])

    return character_set


print(get_char_set('hello'))
