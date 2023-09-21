class TicTacToeModel:
    def __init__(self):
        self.matrix3x3 = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def update_matrix(self, row, column, value):
        if self.matrix3x3[row][column] == ' ':
            self.matrix3x3[row][column] = value
            return True
        return False

    def winner_check(self, value):
        for i in range(3):
            if (self.matrix3x3[i][0] == self.matrix3x3[i][1] == self.matrix3x3[i][2] == value) or \
               (self.matrix3x3[0][i] == self.matrix3x3[1][i] == self.matrix3x3[2][i] == value):
                return True

        # check diagonals
        if (self.matrix3x3[0][0] == self.matrix3x3[1][1] == self.matrix3x3[2][2] == value) or \
           (self.matrix3x3[0][2] == self.matrix3x3[1][1] == self.matrix3x3[2][0] == value):
            return True

        return False
