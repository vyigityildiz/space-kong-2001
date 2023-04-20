import pygame as pg

from Obstacle import *

#TODO: sprite directorysi belli olacak onu ayarla
# Class that specifies the properties of platforms.
class Platform(Obstacle):
    def __init__(self, x: int, y: int, sprite: str) -> None:
        super().__init__(x, y, sprite)