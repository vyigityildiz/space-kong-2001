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
        self.platforms = [[Platform((55 + 60 * i, 610 - i * 2), 64, 24, True) for i in range(14)], [Platform((55 + 60 * i, 450 + i * 2), 64, 24, True) for i in range(12)], [Platform((179 + 60 * i, 338 - i * 2), 64, 24, True) for i in range(12)], [Platform((55 + 60 * i, 178 + i * 2), 64, 24, True) for i in range(12)]]
        self.spaceship = AlienSpaceship((55, 500), 72, 64)

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
        self.spaceship.draw(screen)