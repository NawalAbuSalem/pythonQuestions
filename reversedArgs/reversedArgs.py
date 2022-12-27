def pow(a, b):
    return a ** b


def reversed_args(func):
    def wrapper(*args):
        print(args)
        return func(*args[::-1])

    return wrapper


reversed_pow = reversed_args(pow)
print(reversed_pow(2, 3))
