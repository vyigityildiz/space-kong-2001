from Character import *
from Rock import Rock
import random

# Class that specifies the properties of the enemy
class Enemy(Character):
    def __init__(self, x, y, width, height, sprites: dict, state: str) -> None:
        super().__init__(x, y, width, height, sprites, state)

    def throw_rock(self):
        # Used a prime number to make the random probability lower
        randomizer = random.randint(1, 379)
        if randomizer % 379 == 0:
            return True, Rock(150, 130, 24, 24)
        else:
            return False, None