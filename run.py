from colored import fg, attr
from game import Game
from result import Miss
from target_grid import TargetGrid
from ocean_grid import OceanGrid

import time
import sys


def print_game_board(game):
    ocean_lines = game.players_ocean_grid.make_board()
    target_lines = game.players_target_grid.make_board()

    for i in range(0, len(ocean_lines)):
        divider = '  '
        if i > 1:
            divider = '::'
        print(f"   {ocean_lines[i]}    {divider}    {target_lines[i]}")


# for ship in game.player_ocean_grid.fleet:
#    print(f"Place your {ship.name}, length: {ship.length} (e.g. A, 3)")

##sys.exit(0)

def cleanup_input(user_input):
    clean_input = []
    for ch in user_input:
        if ch.isalnum():
            clean_input.append(ch)
    return "".join(clean_input)


def parse_coordinates(grid_size, coordinate_string):
    coordinates = cleanup_input(coordinate_string)
    print(attr(0))
    # TODO: error checking

    first_coordinate = coordinates[0]
    second_coordinate = coordinates[1:]

    if not first_coordinate.isalpha():
        raise Exception(
            f"First coordinate '{first_coordinate}' should be a letter")

    if not second_coordinate.isnumeric():
        raise Exception(
            f"Second coordinate '{second_coordinate}' should be a number")

    row = first_coordinate.upper()
    column = int(second_coordinate)

    row_number = TargetGrid.ROW_LETTERS.index(row) + 1
    if row_number > grid_size:
        raise Exception(f"Row '{row}' is outside grid")
    if column > grid_size:
        raise Exception(f"Column '{column}' is outside grid")
    return row, column


def print_warning(message):
    print(f"{fg('light_yellow')}{message}{attr(0)}")


def prompt_for_grid_size():
    min_g = OceanGrid.MIN_GRID_SIZE
    max_g = OceanGrid.MAX_GRID_SIZE
    default = f", or hit ENTER for default size ({max_g})"
    prompt = f"Please enter grid size between {min_g} and {max_g}{default}: "

    grid_size = 0

    while grid_size == 0:
        user_input = input(prompt)
        if user_input.strip() == "":
            grid_size = OceanGrid.MAX_GRID_SIZE
        else:
            if user_input.isnumeric():
                grid_size = int(user_input)
                if grid_size < min_g or grid_size > max_g:
                    message = f"{grid_size} is not between {min_g} and {max_g}"
                    print()
                    print_warning(message)
                    print()
                    grid_size = 0  # loop again
            else:
                print()
                print_warning(f"Please enter a number")
                print()
    return grid_size


def main():
    print()
    grid_size = prompt_for_grid_size()
    print()

    # TODO: error checking
    game = Game(int(grid_size))
    game.computers_ocean_grid.randomly_place_all_ships()
    game.players_ocean_grid.randomly_place_all_ships()

    print_game_board(game)

    while not game.is_over():
        print()

        got_coordinates = False
        result = Miss(0, 0)
        while not got_coordinates:
            quit = "- enter Q to quit"
            user_inputs = input(
                f"Enter coordinates (e.g. D5) {quit}: {fg('light_yellow')}")
            if user_inputs.upper().strip() == 'Q':
                print()
                print(f"{fg('light_yellow')}Quitting game. Goodbye!{attr(0)}")
                print()
                sys.exit(0)
            try:
                row, column = parse_coordinates(grid_size, user_inputs)
                row_index = TargetGrid.ROW_LETTERS.index(row)
                column_index = column - 1
                target_grid_data = game.players_target_grid.grid_data
                target = target_grid_data[row_index][column_index]
                if target == TargetGrid.OCEAN_SPACE:
                    got_coordinates = True
                    result = game.user_play(row, column)
                else:
                    coordinates = f"{row}-{column}"
                    print(
                        f"{fg('light_yellow')}You have already attacked {coordinates}{attr(0)}")
                    print()
            except Exception as err:
                print(f"{fg('light_yellow')}{err}{attr(0)}")
                print()

        print_game_board(game)
        print()
        print(
            f"  Player plays {fg('light_yellow')}{result.row}{attr(0)}-{fg('light_yellow')}{result.column}{attr(0)}")
        if result.is_hit:
            if result.is_sunk:
                print(
                    f"  {fg('red')}{attr(1)}HIT{attr(0)} {result.ship_name}: You sunk my {result.ship_name}")
            else:
                print(f"  {fg('red')}{attr(1)}HIT{attr(0)} {result.ship_name}")
        else:
            print(f"  {fg('white')}{attr(1)}MISS{attr(0)}")

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
                        f"  {fg('red')}{attr(1)}HIT{attr(0)} {computer_result.ship_name}: Your {computer_result.ship_name} was sunk")
                else:
                    print(
                        f"  {fg('red')}{attr(1)}HIT{attr(0)} {computer_result.ship_name}")
            else:
                print(f"  {fg('white')}{attr(1)}MISS{attr(0)}")

            if game.is_over():
                print()
                print("  COMPUTER WINS!")
                print()


if __name__ == '__main__':
    main()
