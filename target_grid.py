from colored import fg, bg, attr


class TargetGrid:
    ROW_LETTERS = 'ABCDEFGHIJ'

    OCEAN_SPACE = "~"
    HIT = "X"
    MISS = "!"

    OCEAN_SPACE_COLOR = f"{fg('blue')}~{attr(0)}"
    HIT_COLOR = f"{fg('red')}X{attr(0)}"
    MISS_COLOR = f"{fg('white')}!{attr(0)}"

    def __init__(self, player_name, grid_size):
        self.player_name = player_name
        # TODO: max size 10, min size 2 for grid
        self.grid_data = []
        for i in range(grid_size):
            row = [TargetGrid.OCEAN_SPACE] * grid_size
            self.grid_data.append(row)

    def hit_coordinate(self, row, column):
        self.grid_data[row][column] = TargetGrid.HIT

    def miss_coordinate(self, row, column):
        self.grid_data[row][column] = TargetGrid.MISS

    def make_board(self):
        lines = []
        lines.append(self.player_name)
        lines.append("")
        row_letters = TargetGrid.ROW_LETTERS

        grid_width = len(self.grid_data)  # grid is always square
        col_markers = []
        for col in range(grid_width):
            col_markers.append(str(col + 1))  # grid counts from 1
        lines.append("  " + " ".join(col_markers))

        for r, row in enumerate(self.grid_data):
            row = self.grid_data[r]
            row_with_color = []
            for cell in row:
                if cell == TargetGrid.OCEAN_SPACE:
                    row_with_color.append(TargetGrid.OCEAN_SPACE_COLOR)
                elif cell == TargetGrid.HIT:
                    row_with_color.append(TargetGrid.HIT_COLOR)
                elif cell == TargetGrid.MISS:
                    row_with_color.append(TargetGrid.MISS_COLOR)
            row_cells = " ".join(row_with_color)
            lines.append(f"{row_letters[r]} {row_cells}")
        return lines
