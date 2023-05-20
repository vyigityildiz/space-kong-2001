from Character import *

# Class that specifies the properties of the player. Also has the control methods.
class Player(Character):
    def __init__(self, x, y, width, height, sprites: dict, state: str) -> None:
        super().__init__(x, y, width, height, sprites, state)

    def climb_down(self):
        pass

    def climb_up(self):
        pass

    def jump(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        self.x += 4

    def fall(self):
        self.y += 4