import pygame as pg

# General class for all obstacles; stairs, platforms, and oil drum.
class Obstacle():
    def __init__(self, pos, width, height, sprite) -> None:
        self.pos = pos
        self.size = (width, height)
        self.sprite = sprite
        self._imagetemplate = pg.image.load(self.sprite)
        self._image = pg.transform.scale(self._imagetemplate, (width, height))
        self._rect = self._image.get_rect()