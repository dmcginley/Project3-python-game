from grid import Grid
from game import Game

import time

# GAME LOOP

# while not game.is_over():
#     play()

# player_b_ship_grid = Grid(10)
# player_b_ship_grid.print_board()


# board = []
#
# for i in range(5):
#     board.append(["O"] * 5)
#
#
# def print_board(board_in):
#     for row in board:
#         print(" ".join(row))
#
#
# print_board(board)


# name = input("What is your name?")
# print("hello " + name + "!")

# print("hello " + input("What is your name?") + "!")

grid_size = input("Enter size of game board (4 - 10): ")
# TODO: error checking
game = Game(int(grid_size))
game.player_guess_grid.print_board()

while not game.is_over():
    coordinates = input("Enter coordinates (e.g. D5): ")
    # TODO: error checking
    # TODO: remove all spaces "  A  6" -> "A6"
    row = coordinates[0].upper()
    column = int(coordinates[1:])
    game.user_play(row, column)
    game.player_guess_grid.print_board()
    if game.is_over():
        print(game.result)
    else:
        time.sleep(0.5)
        game.computer_play('B', 1)
        if game.is_over():
            print(game.result)
