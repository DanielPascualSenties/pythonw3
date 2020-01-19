def no_duplicates(lis):
    without_duplicates = []
    for i in range(0, len(lis)):
        if lis[i] in without_duplicates:
            return False
        else:
            without_duplicates.append(lis[i])
    return True


def is_valid_row(row):
    return no_duplicates(row)


def is_valid_column(board, col_number):
    column = [board[0][col_number],
              board[1][col_number],
              board[2][col_number],
              board[3][col_number],
              board[4][col_number],
              board[5][col_number],
              board[6][col_number],
              board[7][col_number],
              board[8][col_number]]
    return no_duplicates(column)


def is_valid_square(board, r, c):
    square = [board[3 * r][3 * c],
              board[3 * r][3 * c + 1],
              board[3 * r][3 * c + 2],
              board[3 * r + 1][3 * c],
              board[3 * r + 1][3 * c + 1],
              board[3 * r + 1][3 * c + 2],
              board[3 * r + 2][3 * c],
              board[3 * r + 2][3 * c + 1],
              board[3 * r + 2][3 * c + 2]]
    return no_duplicates(square)


def is_valid_board(board):
    for i in range(9):
        if not is_valid_row(board[i]):
            print("No válido")
            return False
    print("Filas válidas")
    for i in range(9):
        if not is_valid_column(board, i):
            print("No válida la columna " + str(i))
            return False
    print("Columnas válidas")
    for i in range(3):
        for j in range(3):
            if not is_valid_square(board, i, j):
                print("No válido el cuadradito " + str(i) + " , " + str(j))
                return False
    print("Cuadrados válidos")
    print("Sudoku válido")
    return True


sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [3, 1, 2, 6, 4, 5, 9, 7, 8],
          [9, 7, 8, 3, 1, 2, 6, 4, 5],
          [6, 4, 5, 9, 7, 8, 3, 1, 2],
          [2, 3, 1, 5, 6, 4, 8, 9, 7],
          [8, 9, 7, 2, 3, 1, 5, 6, 4],
          [5, 6, 4, 8, 9, 7, 2, 3, 1],
          ]

is_valid_board(sudoku)
