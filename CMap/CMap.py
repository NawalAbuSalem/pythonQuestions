
def c_map(functions, nums):
    for num in nums:
        x=num
        for function in functions:
            x=function(x)
        yield x


funcs = [lambda x: x*x, lambda x: x+x]
arr = [1, 2, 3, 4]
result=c_map(funcs, arr)
for output in result:
    print(output)

