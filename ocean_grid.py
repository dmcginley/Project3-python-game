import random

from colored import fg, bg, attr

from ship import Ship
from ship import create_ships
from target_grid import TargetGrid

from result import Hit
from result import Miss

from place_ship import Overlap
from place_ship import NoOverlap


class OceanGrid:
    """The grid you place your ships on. A ~ is an empty space. A single lower
    case letter is for a ship. When a ship is hit, I set it to upper case."""

    ROW_LETTERS = 'ABCDEFGHIJ'

    OCEAN_SPACE = "~"
    MISS = "!"

    MIN_GRID_SIZE = 5
    MAX_GRID_SIZE = 10

    def __init__(self, player_name, grid_size):
        self.player_name = player_name
        # TODO: max size 10, min size 2 for grid
        if grid_size < OceanGrid.MIN_GRID_SIZE or grid_size > OceanGrid.MAX_GRID_SIZE:
            raise Exception(
                f"Please enter a grid size between {OceanGrid.MIN_GRID_SIZE} and {OceanGrid.MAX_GRID_SIZE}")
        self.grid_size = grid_size
        self.grid_data = []
        for i in range(grid_size):
            row = [OceanGrid.OCEAN_SPACE] * grid_size
            self.grid_data.append(row)
        self.fleet = create_ships()

    def randomly_place_all_ships(self):
        for ship in self.fleet:
            random_row_index = random.randint(0, self.grid_size - 1)
            random_column_index = random.randint(0, self.grid_size - 1)
            random_orientation = random.choice(["v", "h"])

            result = self.place_ship(ship, random_row_index,
                                     random_column_index, random_orientation)
            while not result.placed:
                random_row_index = random.randint(0, self.grid_size - 1)
                random_column_index = random.randint(0, self.grid_size - 1)
                random_orientation = random.choice(["v", "h"])
                ##print(f"RAND retry {ship.name} | {random_row_index},{random_column_index} : {random_orientation}")
                result = self.place_ship(ship, random_row_index,
                                         random_column_index,
                                         random_orientation)

    def find_ship_by_code(self, code):
        for ship in self.fleet:
            if ship.letter == code:
                return ship
        return None  # if no ship found

    def place_ship(self, ship, row_start, column_start, orientation):
        """place ship in the grid. orientation is 'v' or 'h'.
        If the ship would overlap another ship, returns an Overlap.
        If successful returns NoOverlap."""
        if orientation == 'v':
            return self.place_ship_vertically(ship, row_start, column_start)
        elif orientation == 'h':
            return self.place_ship_horizontally(ship, row_start, column_start)

    def place_ship_vertically(self, ship, row_start, column_start):
        # check edge overlap
        if (ship.length + row_start) > len(self.grid_data):
            return Overlap(f"{ship.name} would overlap edge of ocean grid")
        # check for ship collisions
        empty = OceanGrid.OCEAN_SPACE
        for i in range(0, ship.length):
            if self.grid_data[row_start + i][column_start] != empty:
                # collision with another ship
                ship_code = self.grid_data[row_start + i][column_start]

                other_ship = self.find_ship_by_code(ship_code)
                return Overlap(
                    f"{ship.name} would collide with {other_ship.name}")
        # place ship
        for i in range(0, ship.length):
            self.grid_data[row_start + i][column_start] = ship.letter
        return NoOverlap()

    def place_ship_horizontally(self, ship, row_start, column_start):
        # check edge overlap
        if (ship.length + column_start) > len(self.grid_data):
            return Overlap(f"{ship.name} would overlap edge of ocean grid")
        # check for ship collisions
        empty = OceanGrid.OCEAN_SPACE
        for i in range(0, ship.length):
            if self.grid_data[row_start][column_start + i] != empty:
                # collision with another ship
                ship_code = self.grid_data[row_start][column_start + i]
                other_ship = self.find_ship_by_code(ship_code)
                return Overlap(
                    f"{ship.name} would collide with {other_ship.name}")
        # place ship
        for i in range(0, ship.length):
            self.grid_data[row_start][column_start + i] = ship.letter
        return NoOverlap()

    def is_ship_sunk(self, ship):
        """e.g. Determine if a ship 'a' with length 5 has sunk,
        by looking for 5 upper case 'A's in the grid."""

        hit_points = ship.length
        hit_letter = ship.letter.upper()
        for row in self.grid_data:
            for square in row:
                if square == hit_letter:
                    hit_points = hit_points - 1
        return hit_points <= 0

    def all_ships_sunk(self):
        for ship in self.fleet:
            sunk = self.is_ship_sunk(ship)
            if not sunk:
                return False
        return True

    def call_shot(self, row, column):
        row_letter = OceanGrid.ROW_LETTERS[row]
        column_label = column + 1
        target_square = self.grid_data[row][column]
        if target_square == OceanGrid.OCEAN_SPACE or target_square == OceanGrid.MISS:
            self.grid_data[row][column] = OceanGrid.MISS
            return Miss(row_letter, column_label)
        else:
            self.grid_data[row][column] = target_square.upper()
            hit_ship = None

            for ship in self.fleet:
                if target_square.lower() == ship.letter:
                    hit_ship = ship
                    break
            is_sunk = self.is_ship_sunk(ship)
            row_letter = OceanGrid.ROW_LETTERS[row]
            column_label = column + 1
            return Hit(row_letter, column_label, hit_ship, is_sunk)

    def is_uppercase(self, code):
        return code == code.upper()

    def make_board(self):
        """prints the board into an array of strings, so they can be displayed
        side by side"""
        lines = []
        padding_length = (self.grid_size * 2) - len(self.player_name)

        header_shim = 1
        if self.grid_size > 9:
            header_shim = 2
        padding = " " * (padding_length + header_shim)
        player_name_padded = self.player_name + padding
        lines.append(player_name_padded)
        lines.append("")
        row_letters = 'ABCDEFGHIJ'
        grid_width = len(self.grid_data)  # grid is always square
        col_markers = []
        for col in range(grid_width):
            col_markers.append(str(col + 1))  # grid counts from 1
        lines.append("  " + " ".join(col_markers))

        for r, row in enumerate(self.grid_data):
            row = self.grid_data[r]
            display_row = []
            for cell in row:
                if cell == OceanGrid.OCEAN_SPACE:
                    display_row.append(TargetGrid.OCEAN_SPACE_COLOR)
                elif cell == OceanGrid.MISS:
                    display_row.append(TargetGrid.MISS_COLOR)

                else:
                    if self.is_uppercase(cell):
                        display_row.append(TargetGrid.HIT_COLOR)
                    else:
                        ship_cell = f"{fg('chartreuse_3a')}{cell}{attr(0)}"
                        display_row.append(ship_cell)
            row_cells = " ".join(display_row)
            shim = ''
            if self.grid_size > 9:
                # align with '10' in grid header
                shim = ' '
            lines.append(f"{row_letters[r]} {row_cells}{shim}")
        return lines


def main():
    og = OceanGrid(10)
    for line in og.make_board():
        print(line)


if __name__ == '__main__':
    main()
