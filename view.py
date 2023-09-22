class TicTacToeView:
    def get_user_input(self, value):
        row = int(input(f"Player {value}, enter row (0, 1, 2): "))
        column = int(input(f"Player {value}, enter column (0, 1, 2): "))
        return row, column

    def display_matrix(self, matrix):
        for row in matrix:
            print(" | ".join(row))
            print("-" * 9)
            
    def display_winner(self, value):
        print(f"Player {value} is the winner!")
        
    def display_invalid_move(self):
        print('Invalid move. Please enter different coordinates.')
