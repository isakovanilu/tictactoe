class TicTacToeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play(self):
        while True:
            row, column = self.view.get_user_input(self.model.current_player)
            
            if not self.model.update_matrix(row, column, self.model.current_player):
                self.view.display_invalid_move()
                continue
            
            self.view.display_matrix(self.model.matrix3x3)
            
            if self.model.winner_check(self.model.current_player):
                self.view.display_winner(self.model.current_player)
                break

            self.model.current_player = "O" if self.model.current_player == "X" else "X"
