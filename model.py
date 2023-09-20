class TicTacToeModel:
    def __init__(self):
        self.matrix3x3 = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def update_matrix(self, row, column, value):
        if self.matrix3x3[row][column] == ' ':
            self.matrix3x3[row][column] = value
            return True
        return False
