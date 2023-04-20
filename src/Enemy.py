import pygame as pg

from Character import *
import Rock

# Class that specifies the properties of the enemy
class Enemy(Character):
    def __init__(self) -> None:
        super().__init__()