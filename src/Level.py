from Obstacle import Obstacle
from AlienSpaceship import AlienSpaceship
from Platform import Platform
from Stair import Stair
from Rock import Rock
from Alien import Alien
from Character import Character
from Player import Player
from Enemy import Enemy
import random # used to randomize the stair climbing behavior of aliens
import pygame as pg

# Class that builds and updates the level. Includes the level design, characters, and projectiles. 
class Level():
    def __init__(self) -> None:
        self.platforms = [[Platform((55 + 60 * i, 610 - i * 2), 64, 24, True) for i in range(14)], [Platform((55 + 60 * i, 450 + i * 2), 64, 24, True) for i in range(12)], [Platform((179 + 60 * i, 338 - i * 2), 64, 24, True) for i in range(12)], [Platform((55 + 60 * i, 178 + i * 2), 64, 24, True) for i in range(12)], [Platform((235 + 60 * i, 84), 64, 24, True) for i in range(3)]]
        self.spaceship = AlienSpaceship((55, 500), 72, 56)
        self.stairs = [[Stair((355, 580 - 20 * i), 64, 20) for i in range(7)], [Stair((655, 570 - 20 * i), 64, 20) for i in range(6)], [Stair((475, 444 - 20 * i), 64, 20) for i in range(7)], [Stair((175, 434 - 20 * i), 64, 20) for i in range(6)], [Stair((419, 310 - 20 * i), 64, 20) for i in range(7)], [Stair((719, 300 - 20 * i), 64, 20) for i in range(6)], [Stair((235, 84 + 20 * i), 64, 20) for i in range(5)]]
        self.spacebro = Character(310, 36, 36, 48, {"idle": ["sprites/spacebro-1.png", "sprites/spacebro-2.png"]}, "idle")
        self.robot = Enemy(55, 82, 72, 96, {"idle": ["sprites/robot_idle-1.png", "sprites/robot_idle-2.png"]}, "idle")
        self.player = Player(200, 552, 36, 48, {"idle": ["sprites/spaceplumber-1.png", "sprites/spaceplumber-2.png"]}, "idle")
        self.rocks = [Rock(150, 130, 24, 24)]
        self.aliens = [Alien(80, 550, 21, 24)]
        self.score = 0

    def isNearStairs(self, direction: str, who) -> bool:
        if direction == "up":
            who_interval = who.get_position_interval()
            for stairs in self.stairs:
                for stair in stairs:
                    stair_interval = stair.get_position_interval()
                    if who_interval[0][0] <= stair_interval[1][0] and who_interval[1][0] >= stair_interval[0][0]:
                        if who_interval[1][1] + 2 >= stair_interval[0][1] and who_interval[1][1] - 2 <= stair_interval[1][1]:
                            who.climb_up()
        elif direction == "down":
            who_interval = who.get_position_interval()
            for stairs in self.stairs:
                for stair in stairs:
                    stair_interval = stair.get_position_interval()
                    if who_interval[0][0] <= stair_interval[1][0] and who_interval[1][0] >= stair_interval[0][0]:
                        if who_interval[1][1] - 2 <= stair_interval[0][1]:
                            who.climb_down()

    # Stepping up and moving for aliens and player
    def isStepUp(self, side: str, who):
        if side == "right":
            who_interval =who.get_position_interval()
            for platforms in self.platforms:
                for platform in platforms:
                    platform_interval = platform.get_position_interval()
                    if who_interval[1][1] - 2 == platform_interval[0][1]: # Player's bottom y value and platform's top y value
                        if who_interval[1][0] + 1 == platform_interval[0][0]: # Player x and platform x
                            who.move_up_platforms()
            who.move_right()
        elif side == "left":
            who_interval = who.get_position_interval()
            for platforms in self.platforms:
                for platform in platforms:
                    platform_interval = platform.get_position_interval()
                    if who_interval[1][1] - 2 == platform_interval[0][1]: # Player's bottom y value and platform's top y value
                        if who_interval[0][0] + 1 == platform_interval[1][0]: # Player x and platform x
                            who.move_up_platforms()
            who.move_left()

    def stopAll(self):
        pass

    def resumeAll(self):
        pass

    # Rock and alien movements and deployments
    def control_moving_instances(self):
        # Rock rolling
        for rock in self.rocks:
            rock_interval = rock.get_position_interval()
            if (rock_interval[1][1] >= 450 and rock_interval[1][1] <= 485) or (rock_interval[1][1] >= 178 and rock_interval[1][1] <= 213):
                rock.move("right")
            elif (rock_interval[1][1] >= 585 and rock_interval[1][1] <= 620) or (rock_interval[1][1] >= 303 and rock_interval[1][1] <= 348):
                rock.move("left")

        # Rock throwing
        throw = self.robot.throw_rock()
        if throw[0]:
            self.rocks.append(throw[1])

        # Alien moving including climbing
        for alien in self.aliens:
            alien_interval = alien.get_position_interval()
            index = 0
            # Alien climbing controls
            if not alien.climbing:
                stairs_list = self.stairs.copy()
                for stairs in stairs_list[0:-1]:
                    for stair in stairs:
                        stair_interval = stair.get_position_interval()
                        if ((alien_interval[0][0] + alien_interval[1][0]) // 2) == ((stair_interval[1][0] + stair_interval[0][0]) // 2):
                            if alien_interval[1][1] - 2 >= stair_interval[0][1] and alien_interval[0][1] + 2 <= stair_interval[1][1]:
                                alien.climbing = random.choice([True, False])
                                alien.stairs_index = index
                    index += 1
            if alien.climbing:
                alien.climb_up()
                if ((alien_interval[0][0] + alien_interval[1][0]) // 2) == ((self.stairs[alien.stairs_index][-1].get_position_interval()[1][0] + self.stairs[alien.stairs_index][-1].get_position_interval()[0][0]) // 2):
                    if alien_interval[1][1] - 2 <= self.stairs[alien.stairs_index][-1].get_position_interval()[0][1]:
                        alien.climbing = False
            # alien walking
            if (not alien.climbing) and (not self.is_not_on_platform(alien)):
                if alien.right:
                    if alien_interval[1][0] <= 860:
                        self.isStepUp("right", alien)
                    else:
                        alien.right = False
                elif not alien.right:
                    if alien_interval[0][0] >= 80:
                        self.isStepUp("left", alien)
                    else:
                        alien.right = True

        # Alien Deploying
        deploy = self.spaceship.deploy_alien()
        if deploy[0] and len(self.aliens) <= 20:
            self.aliens.append(deploy[1])

    def object_falling(self):
        for rock in self.rocks:
            if self.is_not_on_platform(rock):
                rock.fall()
        for alien in self.aliens:
            if self.is_not_on_platform(alien):
                alien.fall()

    # On platform check for mainly falling methods of player and rocks
    def is_not_on_platform(self, who):
        who_interval = who.get_position_interval()
        for platforms in self.platforms:
            for platform in platforms:
                platform_interval = platform.get_position_interval()
                if who_interval[1][1] == platform_interval[0][1]: # Player's bottom y value and platform's top y value
                    if who_interval[0][0] <= platform_interval[1][0] and who_interval[1][0] >= platform_interval[0][0]: # Player x and platform x
                        return False
        return True

    # Cumulative rendering method for static obstacle objects to call in the tick method in Game object
    # Static and animated object rendering is not done in the same method to avoid rendering animated objects before starting the game.
    def draw_obstacles(self, screen):
        for floor in self.platforms:
            for platform in floor:
                platform.draw(screen)
        for stairs in self.stairs:
            for stair in stairs:
                stair.draw(screen)

    def remove_fallen_rocks(self):
        if len(self.rocks) != 0:
            if self.rocks[0].get_position_interval()[0][1] >= 720:
                self.rocks.pop(0)

    # Game over check
    def game_over(self):
        player_interval = self.player.get_position_interval()
        # check rocks
        for rock in self.rocks:
            rock_interval = rock.get_position_interval()
            if (rock_interval[0][0] <= player_interval[0][0] and rock_interval[1][0] >= player_interval[0][0]) or (rock_interval[0][0] <= player_interval[1][0] and rock_interval[1][0] >= player_interval[1][0]):
                if (rock_interval[0][1] <= player_interval[0][1] and rock_interval[1][1] >= player_interval[0][1]) or (rock_interval[0][1] <= player_interval[1][1] and rock_interval[1][1] >= player_interval[1][1]):
                    return True
        # check aliens
        for alien in self.aliens:
            alien_interval = alien.get_position_interval()
            if (alien_interval[0][0] <= player_interval[0][0] and alien_interval[1][0] >= player_interval[0][0]) or (alien_interval[0][0] <= player_interval[1][0] and alien_interval[1][0] >= player_interval[1][0]):
                if (alien_interval[0][1] <= player_interval[0][1] and alien_interval[1][1] >= player_interval[0][1]) or (alien_interval[0][1] <= player_interval[1][1] and alien_interval[1][1] >= player_interval[1][1]):
                    return True
        # check if the player fell down
        if player_interval[0][1] >= 720:
            return True
        return False
    
    # game won
    def you_won(self):
        player_interval = self.player.get_position_interval()
        spacebro_interval = self.spacebro.get_position_interval()
        if (spacebro_interval[0][0] <= player_interval[0][0] and spacebro_interval[1][0] >= player_interval[0][0]) or (spacebro_interval[0][0] <= player_interval[1][0] and spacebro_interval[1][0] >= player_interval[1][0]):
            if (spacebro_interval[0][1] <= player_interval[0][1] and spacebro_interval[1][1] >= player_interval[0][1]):
                print("you won")
                return True
        return False
    
    def score_calculation(self, tick):
        if tick % 48:
            self.score += 3
        
    def write_score(self, screen):
        pg.font.init()
        font_to_use = pg.font.SysFont('arial', 35)
        text_surface = font_to_use.render(('Score: ' + str(self.score)), False, (255, 255, 255))
        screen.blit(text_surface, (700,0))

    # Drawing of the animated objects
    def draw_animated_instances(self, screen, frame):
        self.spacebro.draw(screen, frame)
        self.robot.draw(screen, frame)
        self.spaceship.draw(screen, frame)
        self.player.draw(screen, frame)
        for rock in self.rocks:
            rock.draw(screen, frame)
        for alien in self.aliens:
            alien.draw(screen, frame)