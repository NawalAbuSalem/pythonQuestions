def compare_dict(dict_a, dict_b):
    len_a=len(dict_a)
    len_b=len(dict_b)
    if len_a!=len_b:
        return False
    output_list=[key for key in dict_a.keys() if key in dict_b.keys() and dict_a[key] == dict_b[key]]
    return len_a==len(output_list)


dicA = {0: 0, 1: 1, 3: 3}
dicB = {0: 1, 1: 1, 3: 3}
print(compare_dict(dicA, dicB))
