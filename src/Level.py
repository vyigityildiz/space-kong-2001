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
        self.platforms = [[Platform((55 + 60 * i, 610 - i * 2), 64, 24, True) for i in range(14)], [Platform((55 + 60 * i, 450 + i * 2), 64, 24, True) for i in range(12)], [Platform((179 + 60 * i, 338 - i * 2), 64, 24, True) for i in range(12)], [Platform((55 + 60 * i, 178 + i * 2), 64, 24, True) for i in range(12)], [Platform((235 + 60 * i, 84), 64, 24, True) for i in range(2)]]
        self.spaceship = AlienSpaceship((55, 500), 72, 64)
        self.stairs = [[Stair((355, 580 - 20 * i), 64, 20) for i in range(7)], [Stair((655, 570 - 20 * i), 64, 20) for i in range(6)], [Stair((475, 444 - 20 * i), 64, 20) for i in range(7)], [Stair((175, 434 - 20 * i), 64, 20) for i in range(6)], [Stair((419, 310 - 20 * i), 64, 20) for i in range(7)], [Stair((719, 300 - 20 * i), 64, 20) for i in range(6)], [Stair((235, 84 + 20 * i), 64, 20) for i in range(5)]]
        self.spacebro = Character(310, 36, 36, 48, {"idle": ["sprites/spacebro-1.png", "sprites/spacebro-2.png"]}, "idle")

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
        for stairs in self.stairs:
            for stair in stairs:
                stair.draw(screen)
    
    def draw_animated_instances(self, screen, frame):
        self.spacebro.draw(screen, frame)