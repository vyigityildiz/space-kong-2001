import pygame as pg

# Class that specifies the properties of Fireballs.
class Alien():
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = ["sprites/alien-1.png", "sprites/alien-2.png"]
        self.right = True
        self.climbing = False
        self.up = True
        self.stairs_index = None

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def fall(self):
        self.y += 1

    def climb_up(self):
        self.y -= 2

    def move_up_platforms(self):
        self.y -= 2

    def draw(self, screen, frame):
        self._imagetemplate = pg.image.load(self.sprites[frame % len(self.sprites)])
        self._image = pg.transform.scale(self._imagetemplate, (self.width, self.height))
        self._rect = self._image.get_rect()
        screen.blit(self._image, (self.x, self.y))

    def get_position_interval(self):
        top_left = [self.x, self.y]
        bottom_right = [self.x + self.width, self.y + self.height]
        return top_left, bottom_right