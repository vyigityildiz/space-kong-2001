import pygame as pg
import Platform

# Class that specifies the properties of rocks.
class Rock():
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = ["sprites/rock-1.png", "sprites/rock-2.png", "sprites/rock-3.png", "sprites/rock-4.png"]

    def move(self):
        rock_interval = self._get_position_interval()
        if (rock_interval[1][1] >= 450 and rock_interval[1][1] <= 485) or (rock_interval[1][1] >= 178 and rock_interval[1][1] <= 213):
            self.x += 1
        elif (rock_interval[1][1] >= 585 and rock_interval[1][1] <= 620) or (rock_interval[1][1] >= 303 and rock_interval[1][1] <= 348):
            self.x -= 1

    def fall(self):
        self.y += 1

    def draw(self, screen, frame):
        self._imagetemplate = pg.image.load(self.sprites[frame % len(self.sprites)])
        self._image = pg.transform.scale(self._imagetemplate, (self.width, self.height))
        self._rect = self._image.get_rect()
        screen.blit(self._image, (self.x, self.y))

    def _get_position_interval(self):
        top_left = [self.x, self.y]
        bottom_right = [self.x + self.width, self.y + self.height]
        return top_left, bottom_right
    
    def is_at_step(self, platform, side: str):
        if platform.is_instance_at_step(self._get_position_interval(), side):
            self.move_up_platforms()
    
    def is_fallen(self):
        return self._get_position_interval()[0][1] >= 720
    
    def did_player_hit_rock(self, player_interval):
        rock_interval = self._get_position_interval()
        if (rock_interval[0][0] <= player_interval[0][0] and rock_interval[1][0] >= player_interval[0][0]) or (rock_interval[0][0] <= player_interval[1][0] and rock_interval[1][0] >= player_interval[1][0]):
                if (rock_interval[0][1] <= player_interval[0][1] and rock_interval[1][1] >= player_interval[0][1]) or (rock_interval[0][1] <= player_interval[1][1] and rock_interval[1][1] >= player_interval[1][1]):
                    return True
                
    def is_on_platform(self, platform):
        return platform.is_not_on_platform(self._get_position_interval())