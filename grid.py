from colored import fg, bg, attr

class Grid:

    OCEAN_SPACE = f"%s~%s" % (fg('blue'), attr(0))
    HIT = f"%sX%s" % (fg('red'), attr(0))
    #MISS = f"%s!%s" % (fg('dark_slate_gray_3'), attr(0))
    MISS = f"%s!%s" % (fg('white'), attr(0))

    def __init__(self, grid_size):
        print('creating new Grid object here')

        # TODO: max size 10, min size 2 for grid
        self.grid_data = []
        for i in range(grid_size):
            row = [Grid.OCEAN_SPACE] * grid_size
            self.grid_data.append(row)

    def print_board(self):
        # row_letters = ['A', 'B', 'C', 'D']

        row_letters = 'ABCDEFGHIJ'

        # r = 0
        # for row in self.grid_data:
        # for r in range(len(self.grid_data)):

        grid_width = len(self.grid_data)  # grid is always square
        col_markers = []
        for col in range(grid_width):
            col_markers.append(str(col+1))  # grid counts from 1
        print("  " + " ".join(col_markers))

        for r, row in enumerate(self.grid_data):
            row = self.grid_data[r]
            # demo colors for hit and miss
            if r == 1:
                row[0] = Grid.HIT
            if r == 3:
                row[2] = Grid.MISS
            row_cells = " ".join(row)
            print(f"{row_letters[r]} {row_cells}")
            #print(Grid.HIT)
            #print(Grid.MISS)

            # r = r+1

        print('%s Hello World !!! %s more text here' % (fg('red'), attr(0)))