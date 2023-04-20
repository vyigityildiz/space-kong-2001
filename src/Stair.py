import pygame as pg

from Obstacle import *

# Class that specifies the properties of the stairs.
class Stair(Obstacle):
    def __init__(self) -> None:
        super().__init__()