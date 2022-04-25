class Ship:
    def __init__(self, length, name, letter):
        self.length = length
        self.name = name
        self.letter = letter
        self.hit_locations = [False] * length

    # def hit(self, position):
    #     # TODO: error checking
    #     if position >= self.length:
    #         raise Exception("hit position is out of scope")
    #     self.hit_locations[position] = True
    #
    # def is_sunk(self):
    #     for location in self.hit_locations:
    #         if location == False:
    #             return False
    #     return True
    #
    # def __repr__(self):
    #     return str(self.hit_locations)


def create_ships():
    ships = [Ship(5, "Aircraft Carrier", 'a'),
             Ship(4, "Battleship", 'b'),
             Ship(3, "Cruiser", 'c'),
             Ship(3, "Submarine", 's'),
             Ship(2, "Destroyer", 'd')]
    return ships
