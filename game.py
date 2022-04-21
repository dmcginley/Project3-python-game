class Game:

    def __init__(self, board_size):
        self.board_size = board_size
        self.rounds_remaining = 1
        self.result = ''
        print("initializing game....")

    def is_over(self):
        return self.rounds_remaining <= 0

    def user_play(self, row, column):
        print(f"User plays: {row} {column}")
        self.rounds_remaining = self.rounds_remaining - 1
        if self.rounds_remaining == 0:
            self.result = 'User Wins!'

    def computer_play(self, row, column):
        print(f"Computer plays: {row} {column}")
