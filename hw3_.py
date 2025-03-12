def tic_tac_toe(board):
    # Функция для проверки строк
    def check_rows():
        for row in board:
            if all(cell == 'x' or cell == 'X' for cell in row):
                return "x wins!"
            elif all(cell == 'o' or cell == 'O' for cell in row):
                return "o wins!"

    # Функция для проверки столбцов
    def check_columns():
        for col in range(3):
            if all(board[row][col] == 'x' or board[row][col] == 'X' for row in range(3)):
                return "x wins!"
            elif all(board[row][col] == 'o' or board[row][col] == 'O' for row in range(3)):
                return "o wins!"

    # Функция для проверки диагоналей
    def check_diagonals():
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != '-'):
            return f"{board[0][0]} wins!"
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != '-'):
            return f"{board[0][2]} wins!"

    # Проверка наличия пустых клеток (незавершённая игра)
    def has_empty_cells():
        for row in board:
            if '-' in row:
                return True
        return False

    # Проверка на ничью (все клетки заполнены, но никто не выиграл)
    def is_draw():
        if not check_rows() and not check_columns() and not check_diagonals():
            return "draw!"

    # Основная функция
    if check_rows():
        return check_rows()
    if check_columns():
        return check_columns()
    if check_diagonals():
        return check_diagonals()
    if has_empty_cells():
        return "unfinished!"
    return is_draw()


# Тестовые случаи
print(tic_tac_toe([['-', '-', 'o'],
                   ['-', 'x', 'o'],
                   ['x', 'o', 'x']]))  # Ожидаемый результат: "unfinished!"

print(tic_tac_toe([['-', '-', 'o'],
                   ['-', 'o', 'o'],
                   ['x', 'x', 'x']]))  # Ожидаемый результат: "x wins!"
