from target_grid import TargetGrid
import random


class Game:

    def __init__(self, board_size):
        self.board_size = board_size
        self.rounds_remaining = 3
        self.player_ship_grid = TargetGrid(board_size)
        self.player_guess_grid = TargetGrid(board_size)
        self.computer_ship_grid = TargetGrid(board_size)
        self.computer_guess_grid = TargetGrid(board_size)

        self.result = ''

    def is_over(self):
        return self.rounds_remaining <= 0

    # user game grid
    def user_play(self, row, column):
        print(f"User plays: {row} {column}")

        row_index = TargetGrid.ROW_LETTERS.index(row)
        column_index = column - 1
        print(f"... r: {row_index} - c: {column_index}")  # debug

        self.player_guess_grid.hit_coordinate(row_index, column_index)

        self.rounds_remaining = self.rounds_remaining - 1
        if self.rounds_remaining == 0:
            self.result = 'User Wins!'

    # computer game grid
    def computer_play(self, row, column):
        print(f"Computer plays: {row} {column}")

        print("board size is:", self.board_size)
        print(random.randint(0, self.board_size - 1))

        # print(random.randint(1, 4))
        # print(random.choice("a" "b" "c" "d" "e"))
