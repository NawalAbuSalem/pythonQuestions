import re


def get_ex_strings(string):
    return re.findall(r'\bex\w+', string)


print(get_ex_strings("exchange explore hello , get experience"))
