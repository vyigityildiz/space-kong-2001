from Character import *

# Class that specifies the properties of the player. Also has the control methods.
class Player(Character):
    def __init__(self, x, y, width, height, sprites: dict, state: str) -> None:
        super().__init__(x, y, width, height, sprites, state)

    def climb_down(self):
        self.fall()

    def climb_up(self):
        self.y -= 2

    def jump(self):
        pass

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def fall(self):
        self.y += 1

    def move_up_platforms(self):
        self.y -= 2