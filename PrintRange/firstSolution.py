
def get_range(n):
    generated_list = []
    count = 0
    while count <= n:
        generated_list.append(count)
        count += 0.5
    return generated_list


print(get_range(5))
