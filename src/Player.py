import pygame as pg

from Character import *

# Class that specifies the properties of the player. Also has the control methods.
class Player(Character):
    def __init__(self) -> None:
        super().__init__()