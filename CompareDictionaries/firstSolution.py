
def compare_dict(dict_a, dict_b):
    if len(dict_a)!=len(dict_b):
        return False

    for key in dict_a.keys():
        if key in dict_b.keys():
            if dict_a[key] != dict_b[key]:
                return False
        else:
            return False

    return True


dicA = {0: 1, 1: 1, 3: 3}
dicB = {0: 1, 1: 1, 3: 3, 4: 4}
print(compare_dict(dicA, dicB))
