import pygame as pg
from Platform import Platform
import random

# Class that specifies the properties of Fireballs.
class Alien():
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sprites = ["sprites/alien-1.png", "sprites/alien-2.png"]
        self.right = True
        self.climbing = False
        self.up = True
        self.stairs_index = None

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def fall(self):
        self.y += 1

    def climb_up(self):
        self.y -= 2

    def move_up_platforms(self):
        self.y -= 2

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
    
    def did_player_hit_alien(self, player_interval):
        alien_interval = self._get_position_interval()
        if (alien_interval[0][0] <= player_interval[0][0] and alien_interval[1][0] >= player_interval[0][0]) or (alien_interval[0][0] <= player_interval[1][0] and alien_interval[1][0] >= player_interval[1][0]):
            if (alien_interval[0][1] <= player_interval[0][1] and alien_interval[1][1] >= player_interval[0][1]) or (alien_interval[0][1] <= player_interval[1][1] and alien_interval[1][1] >= player_interval[1][1]):
                return True
            
    def is_on_platform(self, platform):
        return platform.is_not_on_platform(self._get_position_interval())
    
    # def is_at_stairs(self, stair, direction):
      #  return stair.is_instance_at_stair(self._get_position_interval(), direction)

    def is_at_stair(self, stair, index):
        if stair.is_alien_at_stair(self._get_position_interval()):
            self.climbing = random.choice([True, False])
            self.stairs_index = index
            return True
        return False

    def is_walking_right(self):
        return self._get_position_interval()[1][0] <= 860
    
    def is_walking_left(self):
        return self._get_position_interval()[0][0] >= 80