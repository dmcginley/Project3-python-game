class Ship:
    def __init__(self, length, name, letter):
        self.length = length
        self.name = name
        self.letter = letter
        self.hit_locations = [False] * length


def create_ships():
    ships = [Ship(5, "Aircraft Carrier", 'a'),
             Ship(4, "Battleship", 'b'),
             Ship(3, "Cruiser", 'c'),
             Ship(3, "Submarine", 's'),
             Ship(2, "Destroyer", 'd')]
    return ships
