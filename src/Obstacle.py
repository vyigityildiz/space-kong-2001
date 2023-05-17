# General class for all obstacles; stairs, platforms, and oil drum.
class Obstacle():
    def __init__(self, pos, width, height, sprite) -> None:
        self.pos = pos
        self.size = (width, height)
        self.sprite = sprite