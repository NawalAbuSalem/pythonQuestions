def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def secondary_order(array, indices, i, j):
    if indices[1][0] == 0:  # secondary asc order
        if array[i][indices[1][0]] > array[j][indices[1][0]]:  # secondary asc get the min
            swap(array, i, j)
    else:  # secondary dsc order
        if array[i][indices[1][0]] < array[j][indices[1][0]]:  # secondary dsc get the min
            print(i, j)
            swap(array, i, j)


def sort(array, indices):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if indices[0][1] == 0:  # primary asc order
                if array[i][indices[0][0]] == array[j][indices[0][0]]:  # secondary order
                    secondary_order(array, indices, i, j)

                if array[i][indices[0][0]] > array[j][indices[0][0]]:  # primary asc get the min
                    swap(array, i, j)

            else:  # primary dsc order
                if array[i][indices[0][0]] == array[j][indices[0][0]]:  # secondary order
                    secondary_order(array, indices, i, j)

                if array[i][indices[0][0]] < array[j][indices[0][0]]:  # primary dsc get the min
                    swap(array, i, j)


arr = [[1, 2, 1], [3, 3, 1], [4, 2, 3], [6, 4, 3]]

index = [[1, 0], [2, 1]]

sort(arr, index)

print(arr)
