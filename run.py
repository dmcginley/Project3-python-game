import random
import sys
from target_grid import TargetGrid
from colored import fg, bg, attr
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

## grid_size = input("Enter size of game board (5 - 10): ")
grid_size = 5  # TODO: ask user for board size

# TODO: error checking
game = Game(int(grid_size))


def print_game_board(game):
    ocean_lines = game.player_ocean_grid.make_board()
    target_lines = game.player_target_grid.make_board()

    for i in range(0, len(ocean_lines)):
        divider = '  '
        if i > 1:
            divider = '::'
        print(f"   {ocean_lines[i]}    {divider}    {target_lines[i]}")


game.computer_ocean_grid.randomly_place_all_ships()
game.player_ocean_grid.randomly_place_all_ships()

print_game_board(game)

# for ship in game.player_ocean_grid.fleet:
#    print(f"Place your {ship.name}, length: {ship.length} (e.g. A, 3)")

##sys.exit(0)

while not game.is_over():
    print()
    coordinates = input(f"Enter coordinates (e.g. D5): {fg('light_yellow')}")
    print(attr(0))
    # TODO: error checking
    # TODO: remove all spaces "  A  6" -> "A6"
    row = coordinates[0].upper()
    column = int(coordinates[1:])

    result = game.user_play(row, column)
    print_game_board(game)
    print()
    print(
        f"  Player plays {fg('light_yellow')}{result.row}{attr(0)}-{fg('light_yellow')}{result.column}{attr(0)}")
    if result.is_hit:
        if result.is_sunk:
            print(
                f"  {fg('red')}HIT{attr(0)} {result.ship_name}: You sunk my {result.ship_name}")
        else:
            print(f"  {fg('red')}HIT{attr(0)} {result.ship_name}")
    else:
        print(f"  {fg('white')}MISS{attr(0)}")

    if game.is_over():
        print()
        print("  YOU WIN!")
        print()
    else:
        print()
        time.sleep(1.5)
        computer_result = game.computer_play()
        print_game_board(game)
        print()
        print(
            f"  Computer plays {fg('light_yellow')}{computer_result.row}{attr(0)}-{fg('light_yellow')}{computer_result.column}{attr(0)}")
        if computer_result.is_hit:
            if computer_result.is_sunk:
                print(
                    f"  {fg('red')}HIT{attr(0)} {computer_result.ship_name}: Your {computer_result.ship_name} was sunk")
            else:
                print(f"  {fg('red')}HIT{attr(0)} {computer_result.ship_name}")
        else:
            print(f"  {fg('white')}MISS{attr(0)}")

        if game.is_over():
            print()
            print("  COMPUTER WINS!")
            print()
