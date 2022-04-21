from grid import Grid
from game import Game

player_a_ship_grid = Grid(4)
player_a_ship_grid.print_board()

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


game = Game(2)

while not game.is_over():
    coordinates = input("Enter coordinates (e.g. D5): ")
    # TODO: error checking
    # TODO: remove all spaces "  A  6" -> "A6"
    row = coordinates[0].upper()
    column = int(coordinates[1])
    game.user_play(row, column)
    if game.is_over():
        print(game.result)
    else:
        game.computer_play('B', 1)
        if game.is_over():
            print(game.result)
