import pygame as pg

# General class for charcters; enemy, player and the princess.
class Character():
    def __init__(self, x, y, width, height, sprites: dict, state: str) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = sprites
        # states are the state the character in such as idle, running, and climbing. If the character is not a
        # special character, like Player, it will only have idle state
        self.state = state

    def draw(self, screen, frame):
        self._imagetemplate = pg.image.load(self.sprites[self.state][frame % len(self.sprites[self.state])])
        self._image = pg.transform.scale(self._imagetemplate, (self.width, self.height))
        self._rect = self._image.get_rect()
        screen.blit(self._image, (self.x, self.y))

    def get_position_interval(self):
        top_left = [self.x, self.y]
        bottom_right = [self.x + self.width, self.y + self.height]
        return top_left, bottom_right