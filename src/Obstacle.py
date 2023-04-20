import pygame as pg

# General class for all obstacles; stairs, platforms, and oil drum.
class Obstacle():
    """Class constructor

    Args:
        x pixel x coordinate value
        y pixel y coordinate value
        sprite directory of the sprite png
    """
    def __init__(self, x: int, y: int, sprite: str) -> None:
        self.pos = (x, y)
        self.sprite = sprite