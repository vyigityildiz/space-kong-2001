from Obstacle import *
import pygame as pg

# Class that specifies the properties of platforms.
class Platform(Obstacle):
    def __init__(self, pos, width, height, isOverAStair) -> None:
        super().__init__(pos, width, height, "sprites/platform.png")
        self.isOverAStair = isOverAStair

    def draw(self, screen):
        screen.blit(self._image, self.pos)