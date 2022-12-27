
# time comp(O(n*(max row length+max row length)))
# space comp(O(1))

def lambda_map(matrix):
    square = lambda x: x * x
    for array in matrix:
        for num in array:
            if num <= 0:
                array.remove(num)

        for index in range(len(array)):
            array[index] = square(array[index])


arr = [[-1, 1, 2, -2, 6], [3, 4, -5]]
lambda_map(arr)
print(arr)
