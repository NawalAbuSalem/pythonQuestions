
def get_ex_strings(string):
    output_list = []
    words = string.split(" ")
    for word in words:
        if word.startswith("ex"):
            output_list.append(word)
    return output_list


print(get_ex_strings("exchange explore hello , get experience"))
