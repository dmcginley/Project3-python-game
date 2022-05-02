from target_grid import TargetGrid
from ocean_grid import OceanGrid
import random


class Game:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_ocean_grid = OceanGrid("Player", grid_size)
        self.player_target_grid = TargetGrid("Computer", grid_size)
        self.computer_ocean_grid = OceanGrid("Computer", grid_size)
        self.computer_target_grid = TargetGrid("Target", grid_size)

        self.result = ''

    def is_over(self):
        computer_wins = self.player_ocean_grid.all_ships_sunk()
        player_wins = self.computer_ocean_grid.all_ships_sunk()
        return computer_wins or player_wins

    # user game grid
    def user_play(self, row, column):
        #  change row letter to row index (e.g. B -> 1), and column to column index (e.g. 1 -> 0)
        row_index = TargetGrid.ROW_LETTERS.index(row)
        column_index = column - 1

        result = self.computer_ocean_grid.call_shot(row_index, column_index)
        if result.is_hit:
            self.player_target_grid.hit_coordinate(row_index, column_index)
        else:
            self.player_target_grid.miss_coordinate(row_index, column_index)

        return result

    # computer game grid
    def computer_play(self):

        row_index, column_index = self.computer_choose_coordinates_randomly()
        row = OceanGrid.ROW_LETTERS[row_index]
        column = column_index + 1

        result = self.player_ocean_grid.call_shot(row_index, column_index)

        if result.is_hit:
            self.computer_target_grid.hit_coordinate(row_index, column_index)
        else:
            self.computer_target_grid.miss_coordinate(row_index, column_index)
        return result

    def computer_choose_coordinates_randomly(self):
        random_row_index = random.randint(0, self.grid_size - 1)
        random_column_index = random.randint(0, self.grid_size - 1)

        cell = self.computer_target_grid.grid_data[random_row_index][
            random_column_index]
        while cell == TargetGrid.HIT or cell == TargetGrid.MISS:
            # print("guessing again...")
            random_row_index = random.randint(0, self.grid_size - 1)
            random_column_index = random.randint(0, self.grid_size - 1)

            cell = self.computer_target_grid.grid_data[random_row_index][
                random_column_index]

        return random_row_index, random_column_index
