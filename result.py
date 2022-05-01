class Result:
    def __init__(self, row, column, is_hit):
        self.row = row
        self.column = column
        self.is_hit = is_hit


class Miss(Result):
    def __init__(self, row, column):
        Result.__init__(self, row, column, False)

    def __repr__(self):
        return "Miss"


class Hit(Result):
    def __init__(self, row, column, ship, is_sunk):
        Result.__init__(self, row, column, True)
        self.ship_name = ship.name
        self.is_sunk = is_sunk

    def __repr__(self):
        sunk = ''
        if self.is_sunk:
            sunk = '; ship sunk'
        return f"Hit {self.ship_name}{sunk}"
