class PlacementResult:
    def __init__(self, placed):
        self.placed = placed


class NoOverlap(PlacementResult):
    def __init__(self):
        PlacementResult.__init__(self, True)

    def __repr__(self):
        return "No Overlap"


class Overlap(PlacementResult):
    def __init__(self, message):
        PlacementResult.__init__(self, False)
        self.message = message

    def __repr__(self):
        return f"Overlap ({self.message})"
