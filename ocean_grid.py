from colored import fg, bg, attr

from ship import Ship
from ship import create_ships
from target_grid import TargetGrid

from result import Hit
from result import Miss


class OceanGrid:
    """The grid you place your ships on. A ~ is an empty space. A single lower case letter
    is for a ship. When a ship is hit, I set it to upper case."""

    ROW_LETTERS = 'ABCDEFGHIJ'

    OCEAN_SPACE = "~"
    MISS = "!"

    MIN_GRID_SIZE = 5
    MAX_GRID_SIZE = 10

    def __init__(self, grid_size):
        # TODO: max size 10, min size 2 for grid
        if grid_size < OceanGrid.MIN_GRID_SIZE or grid_size > OceanGrid.MAX_GRID_SIZE:
            raise Exception(f"Please enter a grid size between {OceanGrid.MIN_GRID_SIZE} and {OceanGrid.MAX_GRID_SIZE}")
        self.grid_data = []
        for i in range(grid_size):
            row = [OceanGrid.OCEAN_SPACE] * grid_size
            self.grid_data.append(row)
        self.fleet = create_ships()

        # hardcode : place one ship

        aircraft_carrier = self.fleet[0]
        cruiser = self.fleet[2]
        destroyer = self.fleet[4]
        a = self.place_ship(aircraft_carrier, 0, 0, 'h')
        c = self.place_ship(cruiser, 2, 1, 'v')
        d = self.place_ship(destroyer, 4, 3, 'h')
        # print(f"a: {a}, c: {c}, d: {d}")

    def place_ship(self, ship, row_start, column_start, orientation):
        """place ship in the grid. orientation is 'v' or 'h'.
        If the ship would overlap another ship, return False. If successful returns True."""
        print(f"Placing '{ship.name}' at {row_start},{column_start} / {orientation}")
        if orientation == 'v':
            # vertical
            if (ship.length + row_start) > len(self.grid_data):
                print("outside ocean grid")
                return False
            # check for collisions
            for i in range(0, ship.length):
                print(f"CHECK v: {row_start + i},{column_start}")
                if self.grid_data[row_start + i][column_start] != OceanGrid.OCEAN_SPACE:
                    # collision with another ship
                    return False
            # place ship
            for i in range(0, ship.length):
                print(f"v: {row_start + i},{column_start}")
                self.grid_data[row_start + i][column_start] = ship.letter
        elif orientation == 'h':
            # horizontal
            if (ship.length + column_start) > len(self.grid_data):
                print("outside ocean grid")
                return False
            # check for collisions
            for i in range(0, ship.length):
                print(f"CHECK h: {row_start},{column_start + i}")
                if self.grid_data[row_start][column_start + i] != OceanGrid.OCEAN_SPACE:
                    # collision with another ship
                    return False
            # place ship
            for i in range(0, ship.length):
                print(f"CHECK h: {row_start},{column_start + i}")
                self.grid_data[row_start][column_start + i] = ship.letter
            # place
            # for i in range(0, ship.length):
            #     print(f"h: {row},{column + i}")
            #     self.grid_data[row][column + i] = ship.letter
        return True

    def is_ship_sunk(self, ship):
        """e.g. Determine if a ship 'a' with length 5 has sunk, by looking for 5 upper case 'A's in the grid."""

        hit_points = ship.length
        hit_letter = ship.letter.upper()
        print(f" is ship sunk?? hit point for {ship.name} = {hit_points} - searching for {hit_letter}")
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
        target_square = self.grid_data[row][column]
        print(f"target_square = {target_square}")
        if target_square == OceanGrid.OCEAN_SPACE:
            print("Miss!")
            self.grid_data[row][column] = OceanGrid.MISS
            return Miss()
        else:
            print(f"HIT! ship {target_square}")
            self.grid_data[row][column] = target_square.upper()
            hit_ship = None
            for ship in self.fleet:
                if target_square == ship.letter:
                    hit_ship = ship
                    break
            is_sunk = self.is_ship_sunk(ship)
            return Hit(hit_ship, is_sunk)

    def make_board(self):
        """prints the board into an array of strings, so they can be displayed side by side"""
        lines = []
        row_letters = 'ABCDEFGHIJ'
        grid_width = len(self.grid_data)  # grid is always square
        col_markers = []
        for col in range(grid_width):
            col_markers.append(str(col + 1))  # grid counts from 1
        lines.append("  " + " ".join(col_markers))

        for r, row in enumerate(self.grid_data):
            row = self.grid_data[r]
            display_row = []
            for square in row:
                if square == OceanGrid.OCEAN_SPACE:
                    display_row.append(TargetGrid.OCEAN_SPACE)
                else:
                    display_row.append(square)
            row_cells = " ".join(display_row)
            lines.append(f"{row_letters[r]} {row_cells}")
        return lines


def main():
    og = OceanGrid(6)
    ships = create_ships()
    aircraft_carrier = ships[0]
    og.place_ship(aircraft_carrier, 1, 1, 'v')  # == B 2
    patrol_boat = ships[1]
    og.place_ship(patrol_boat, 2, 3, 'h')  # == C 4
    og.make_board()
    print(og.call_shot(0, 1))
    og.make_board()
    print(og.call_shot(2, 3))
    og.make_board()
    print(og.call_shot(3, 3))
    og.make_board()

    print(og.is_ship_sunk(patrol_boat))
    print("-------------------")

    print(f"{bg('grey_30')}{fg('white')}a a{attr(0)}")
    print()
    print(f"{bg('grey_30')}{fg('white')}b{attr(0)}")

    print(f"{bg('grey_30')}{fg('white')}b{attr(0)}")


if __name__ == '__main__':
    main()
    # def hit_coordinate(self, row, column):
    #     self.grid_data[row][column] = TargetGrid.HIT
    #
    # def miss_coordinate(self, row, column):
    #     self.grid_data[row][column] = TargetGrid.MISS
    #
    # def print_board(self):
    #     # row_letters = ['A', 'B', 'C', 'D']
    #
    #     row_letters = 'ABCDEFGHIJ'
    #
    #     # r = 0
    #     # for row in self.grid_data:
    #     # for r in range(len(self.grid_data)):
    #
    #     grid_width = len(self.grid_data)  # grid is always square
    #     col_markers = []
    #     for col in range(grid_width):
    #         col_markers.append(str(col + 1))  # grid counts from 1
    #     print("  " + " ".join(col_markers))
    #
    #     for r, row in enumerate(self.grid_data):
    #         row = self.grid_data[r]
    #         # demo colors for hit and miss
    #         # if r == 1:
    #         #     row[0] = Grid.HIT
    #         # if r == 3:
    #         #     row[2] = Grid.MISS
    #         row_cells = " ".join(row)
    #         print(f"{row_letters[r]} {row_cells}")
    #         # print(Grid.HIT)
    #         # print(Grid.MISS)
    #
    #         # r = r+1
