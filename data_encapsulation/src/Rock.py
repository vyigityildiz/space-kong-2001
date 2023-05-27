import pygame as pg

# Class that specifies the properties of rocks.
class Rock():
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = ["sprites/rock-1.png", "sprites/rock-2.png", "sprites/rock-3.png", "sprites/rock-4.png"]

    def move(self, side: str):
        if side == "right":
            self.x += 1
        elif side == "left":
            self.x -= 1

    def fall(self):
        self.y += 1

    def draw(self, screen, frame):
        self._imagetemplate = pg.image.load(self.sprites[frame % len(self.sprites)])
        self._image = pg.transform.scale(self._imagetemplate, (self.width, self.height))
        self._rect = self._image.get_rect()
        screen.blit(self._image, (self.x, self.y))

    def get_position_interval(self):
        top_left = [self.x, self.y]
        bottom_right = [self.x + self.width, self.y + self.height]
        return top_left, bottom_right