import pygame as pg

from Obstacle import *
import Alien

# Class that specifies the properties of oil drum.
class AlienSpaceship(Obstacle):
    def __init__(self) -> None:
        super().__init__()