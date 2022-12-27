cols = set()
diagonal1 = set()
diagonal2 = set()


def fill_queens(board, row, n):
    if row >= n:
        print(board)
        return True

    is_pattern_found = False
    for col in range(n):
        if col in cols or (row + col) in diagonal1 or (row - col) in diagonal2:
            continue

        cols.add(col)
        diagonal1.add(row + col)
        diagonal2.add(row - col)
        board[row][col] = 1

        is_pattern_found = is_pattern_found or fill_queens(board, row + 1, n)

        cols.remove(col)
        diagonal1.remove(row + col)
        diagonal2.remove(row - col)
        board[row][col] = 0

    return is_pattern_found


def can_organize_the_board(board, n):
    if fill_queens(board, 0, n):
        print("yes")
    else:
        print("No")


num = 10
chess = [[0 for x in range(num)] for y in range(num)]
can_organize_the_board(chess, num)
