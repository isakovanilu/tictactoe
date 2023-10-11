class TicTacToeModel:
    def __init__(self):
        self.matrix3x3 = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def update_matrix(self, row, column, value):
        if self.matrix3x3[row][column] == ' ':
            self.matrix3x3[row][column] = value
            return True
        return False
    
    def _check_rows(self, value):
        return any(all(cell == value for cell in row) for row in self.matrix3x3)
    
    def _check_columns(self, value):
        return any(all(self.matrix3x3[row][col] == value for row in range(3)) for col in range(3))

    def _check_diagonals(self, value):
        return all(self.matrix3x3[i][i] == value for i in range(3)) or \
               all(self.matrix3x3[i][2 - i] == value for i in range(3))


    