import pygame as pg

# General class for all obstacles; stairs, platforms, and oil drum.
class Obstacle():
    def __init__(self, x, y) -> None:
        self.pos = (x, y)