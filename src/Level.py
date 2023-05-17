from Obstacle import Obstacle
from AlienSpaceship import AlienSpaceship
from Platform import Platform
from Stair import Stair
from Rock import Rock
from Alien import Alien
from Character import Character
from Player import Player
from Enemy import Enemy

# Class that builds and updates the level. Includes the level design, characters, and projectiles. 
class Level():
    def __init__(self) -> None:
        self.platforms = [[Platform((55 + 60 * i, 560 - i * 2), 64, 24, True) for i in range(14)], [Platform((55 + 60 * i, 400 + i * 2), 64, 24, True) for i in range(12)], [Platform((179 + 60 * i, 288 - i * 2), 64, 24, True) for i in range(12)], [Platform((55 + 60 * i, 128 + i * 2), 64, 24, True) for i in range(12)]]

    def isNearStairs(self) -> bool:
        pass

    def canJump(self) -> bool:
        pass

    def isEmpty(self) -> bool:
        pass

    def stopAll(self):
        pass

    def resumeAll(self):
        pass

    def loadLevel(self):
        pass

    def control_moving_instances(self):
        pass

    def draw_obstacles(self, screen):
        for floor in self.platforms:
            for platform in floor:
                platform.draw(screen)