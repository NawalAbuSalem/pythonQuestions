
# time comp(O(n*(max row length+max row length)))
# space comp(O(n* max row length))

def lambda_map(matrix):
    square = lambda x: x * x
    new_matrix = []
    for array in matrix:
        new_array = []
        for num in array:
            if num > 0:
                new_array.append(square(num))

        new_matrix.append(new_array)

    return new_matrix


arr = [[-1, 1, 2, -2, 6], [3, 4, -5]]
print(lambda_map(arr))
