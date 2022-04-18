class Grid:
    def __init__(self, grid_size):
        print('creating new Grid object here')
        self.grid_data = []
        for i in range(grid_size):
            row = ["~"] * grid_size
            self.grid_data.append(row)

    def print_board(self):
        row_letters = ['A', 'B', 'C', 'D']

        #r = 0
        #for row in self.grid_data:
        #for r in range(len(self.grid_data)):
        grid_width = len(self.grid_data) # grid is always square
        col_markers = []
        for col in range(grid_width):
            col_markers.append(str(col+1)) # grid counts from 1
        print("  " + " ".join(col_markers))

        for r, row in enumerate(self.grid_data):
            row = self.grid_data[r]
            row_cells = " ".join(row)
            print(f"{row_letters[r]} {row_cells}")
            #r = r+1


