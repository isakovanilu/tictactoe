class TicTacToeView:
    def get_user_input(self, value):
        row = int(input(f"Player {value}, enter row (0, 1, 2): "))
        column = int(input(f"Player {value}, enter column (0, 1, 2): "))
        return row, column

    def display_matrix(self, matrix):
        for row in matrix:
            print(" | ".join(row))
            print("-" * 9)
            
