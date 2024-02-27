class Board:
    """Класс, который описывает игровое поле."""
    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(self.field_size)]
                      for _ in range(self.field_size)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player):
        count_row_marks = 0
        count_col_marks = 0
        count_main_diag_marks = 0
        count_side_diag_marks = 0
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == player:
                    count_row_marks += 1
                if self.board[j][i] == player:
                    count_col_marks += 1
                if i == j and self.board[i][j] == player:
                    count_main_diag_marks += 1
                if i == self.field_size - j - 1 and self.board == player:
                    count_side_diag_marks += 1
            if (count_row_marks == self.field_size or
                    count_col_marks == self.field_size):
                return True
            else:
                count_row_marks = 0
                count_col_marks = 0
        if (count_main_diag_marks == self.field_size or
                count_side_diag_marks == self.field_size):
            return True
        return False

    def __str__(self):
        return ('Объект игрового поля размером '
                f'{self.field_size}x{self.field_size}')
