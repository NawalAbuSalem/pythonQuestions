import math


def accumulator():
    # print("sum before while: ",sum)
    sum = 0
    while True:
        sum += yield sum
        # print("sum after while: ",sum)
        yield sum


def squarer():
    while True:
        number = yield
        yield number ** 2


def rooter():
    while True:
        number = yield
        yield math.floor(math.sqrt(number))


nums = [1, 2, 3]
order = [squarer(), accumulator()]
for operation in order:
    for numIndex in range(len(nums)):
        next(operation)
        nums[numIndex] = operation.send(nums[numIndex])

print(nums[-1])
