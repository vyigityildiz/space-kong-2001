from Obstacle import *

# Class that specifies the properties of the stairs.
class Stair(Obstacle):
    def __init__(self, pos, width, height) -> None:
        super().__init__(pos, width, height, "sprites/stair.png")

    def draw(self, screen):
        screen.blit(self._image, self.pos)