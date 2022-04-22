from colored import fg, bg, attr

from ship import create_ships


class OceanGrid:
    ROW_LETTERS = 'ABCDEFGHIJ'

    OCEAN_SPACE = "~"
    MISS = "!"

    def __init__(self, grid_size):
        # TODO: max size 10, min size 2 for grid
        self.grid_data = []
        for i in range(grid_size):
            row = [OceanGrid.OCEAN_SPACE] * grid_size
            self.grid_data.append(row)

    def place_ship(self, ship, row, column, orientation):
        self.grid_data[row][column] = ship.letter
        # TODO: this only places first square of ship

    def is_ship_sunk(self, ship):
        hit_points = ship.length
        hit_letter = ship.letter.upper()
        print(f" is ship sunk?? hit point for {ship.name} = {hit_points} - searching for {hit_letter}")
        for row in self.grid_data:
            for square in row:
                if square == hit_letter:
                    hit_points = hit_points - 1
        return hit_points <= 0

    def call_shot(self, row, column):
        target_square = self.grid_data[row][column]
        print(f"target_square = {target_square}")
        if target_square == OceanGrid.OCEAN_SPACE:
            print("Miss!")
            self.grid_data[row][column] = OceanGrid.MISS
            return False
        else:
            print(f"HIT! ship {target_square}")
            self.grid_data[row][column] = target_square.upper()
            return True

    def print_grid(self):
        row_letters = 'ABCDEFGHIJ'
        grid_width = len(self.grid_data)  # grid is always square
        col_markers = []
        for col in range(grid_width):
            col_markers.append(str(col + 1))  # grid counts from 1
        print("  " + " ".join(col_markers))

        for r, row in enumerate(self.grid_data):
            row = self.grid_data[r]
            row_cells = " ".join(row)
            print(f"{row_letters[r]} {row_cells}")


def main():
    og = OceanGrid(4)
    ships = create_ships()
    aircraft_carrier = ships[0]
    og.place_ship(aircraft_carrier, 1, 1, 'v')  # == B 2
    patrol_boat = ships[1]
    og.place_ship(patrol_boat, 2, 3, 'h')  # == C 4
    og.print_grid()
    og.call_shot(0, 1)
    og.print_grid()
    og.call_shot(2, 3)
    og.print_grid()
    og.call_shot(3, 3)
    og.print_grid()

    print(og.is_ship_sunk(patrol_boat))

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
