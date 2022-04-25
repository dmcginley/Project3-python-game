from target_grid import TargetGrid
from ocean_grid import OceanGrid
import random


class Game:

    def __init__(self, board_size):
        self.board_size = board_size
        self.rounds_remaining = 5
        self.player_ocean_grid = OceanGrid(board_size)
        self.player_target_grid = TargetGrid(board_size)
        self.computer_ocean_grid = OceanGrid(board_size)

        # hard-code a computer ship
        # self.computer_ocean_grid.grid_data[0][0] = 's'
        # self.computer_ocean_grid.grid_data[0][1] = 's'
        # self.computer_ocean_grid.grid_data[0][2] = 's'

        # self.player_ocean_grid.grid_data[0][0] = 'c'
        # self.player_ocean_grid.grid_data[1][0] = 'c'
        # self.player_ocean_grid.grid_data[2][0] = 'c'

        self.computer_target_grid = TargetGrid(board_size)

        self.result = ''

    def is_over(self):
        # return self.player_ocean_grid.all_ships_sunk() or self.computer_ocean_grid.all_ships_sunk()
        return self.rounds_remaining <= 0

    # user game grid
    def user_play(self, row, column):
        print(f"User plays: {row} {column}")
        #  change row letter to row index (e.g. B -> 1), and column to column index (e.g. 1 -> 0)
        row_index = TargetGrid.ROW_LETTERS.index(row)
        column_index = column - 1
        print(f"... r: {row_index} - c: {column_index}")  # debug

        result = self.computer_ocean_grid.call_shot(row_index, column_index)
        if result.is_hit:
            self.player_target_grid.hit_coordinate(row_index, column_index)
            print(f">>> HIT {result.ship_name}")
            if result.is_sunk:
                print(f">>> You sunk my {result.ship_name}")
        else:
            self.player_target_grid.miss_coordinate(row_index, column_index)

        self.rounds_remaining = self.rounds_remaining - 1
        if self.rounds_remaining == 0:
            self.result = 'User Wins!'

    # computer game grid
    def computer_play(self, row, column):
        print(f"Computer plays: {row} {column}")

        print("board size is:", self.board_size)
        print(random.randint(0, self.board_size - 1))
