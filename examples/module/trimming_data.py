class TrimmingData():
    def __init__(self, position: tuple, size: tuple, needs_trimming: bool):
        self.position = position
        self.size = size
        self.needs_trimming = needs_trimming