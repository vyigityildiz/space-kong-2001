import pygame as pg

from Obstacle import *

# Class that specifies the properties of platforms.
class Platform(Obstacle):
    def __init__(self) -> None:
        super().__init__()