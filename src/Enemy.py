from Character import *
import Rock
import random

# Class that specifies the properties of the enemy
class Enemy(Character):
    def __init__(self, x, y, width, height, sprites: dict, state: str) -> None:
        super().__init__(x, y, width, height, sprites, state)

    def throw_rock(self, frame):
        pass