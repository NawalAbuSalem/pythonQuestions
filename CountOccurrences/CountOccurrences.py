
def count_occurrences(string):
    dic = {}
    for char in string:
        if char in dic.keys():
            dic[char] += 1
        else:
            dic[char] = 1

    return dic


print(count_occurrences("hello"))


