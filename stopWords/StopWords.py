import re


def stop_words(text, k):
    words = re.findall(r'\b\w+\b', text)
    dict = {}
    result = []
    for word in words:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict[word] = 1
    for item in dict.items():
        if item[1] >= k:
            result.append(item[0])
    return result


print(stop_words("a mouse is smaller than a dog but a dog is stronger", 2))
