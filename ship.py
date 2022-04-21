class Ship:
    def __init__(self, length):
        self.length = length
        self.hit_locations = [False] * length

    def hit(self, position):
        # TODO: error checking
        if position >= self.length:
            raise Exception("hit position is out of scope")
        self.hit_locations[position] = True

    def is_sunk(self):
        for location in self.hit_locations:
            if location == False:
                return False
        return True

    def __repr__(self):
        return str(self.hit_locations)


if __name__ == '__main__':
    s = Ship(4)
    s.hit(0)
    s.hit(1)
    s.hit(2)
    s.hit(3)
    print(s)
    print(s.is_sunk())

