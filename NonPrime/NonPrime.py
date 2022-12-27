def get_next_positive():
    n = 1
    while True:
        yield n
        n += 1


def is_not_prime(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


def get_non_prime(generator, k):
    non_prime_list = []
    while k != 0:
        num = next(generator)
        if is_not_prime(num):
            k -= 1
            non_prime_list.append(num)

    return non_prime_list


print(get_non_prime(get_next_positive(), 10))
