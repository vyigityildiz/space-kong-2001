from Obstacle import *
import pygame as pg
from Player import Player
from Rock import Rock

# Class that specifies the properties of platforms.
class Platform(Obstacle):
    def __init__(self, pos, width, height, isOverAStair) -> None:
        super().__init__(pos, width, height, "sprites/platform.png")

    # Rendering method
    def draw(self, screen):
        screen.blit(self._image, self.pos)

    def is_instance_at_step(self, who_interval, side):
        if side == "right":
            platform_interval = self._get_position_interval()
            if who_interval[1][1] - 2 == platform_interval[0][1]: # Player's bottom y value and platform's top y value
                if who_interval[1][0] + 1 == platform_interval[0][0]: # Player x and platform x
                    return True
            return False
        elif side == "left":
            platform_interval = self._get_position_interval()
            if who_interval[1][1] - 2 == platform_interval[0][1]: # Player's bottom y value and platform's top y value
                if who_interval[0][0] + 1 == platform_interval[1][0]: # Player x and platform x
                    return True
            return False
        
    def is_not_on_platform(self, who_interval):
        platform_interval = self._get_position_interval()
        if who_interval[1][1] == platform_interval[0][1]: # Player's bottom y value and platform's top y value
            if who_interval[0][0] <= platform_interval[1][0] and who_interval[1][0] >= platform_interval[0][0]: # Player x and platform x
                return True
        return False