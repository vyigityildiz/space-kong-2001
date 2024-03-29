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
        # List to track which aliens are climbing whenever an alien is deployed False is appended to this list and this list is only manipulated when an alien is climbing
        self.alien_climbing = [False]
        self.score = 0

    def isNearStairs(self, direction: str, who) -> bool:
        if direction == "up":
            for stairs in self.stairs:
                for stair in stairs:
                    if who.is_at_stairs(stair, direction):
                        who.climb_up()
        elif direction == "down":
            for stairs in self.stairs:
                for stair in stairs:
                    if who.is_at_stairs(stair, direction):
                        who.climb_down()

    # Stepping up and moving for aliens and player
    def isStepUp(self, side: str, who):
        for platforms in self.platforms:
            for platform in platforms:
                who.is_at_step(platform, side)
        if side == "right":
            who.move_right()
        elif side == "left":
            who.move_left()

    # Rock and alien movements and deployments
    def control_moving_instances(self):
        # Rock rolling
        for rock in self.rocks:
            rock.move()

        # Rock throwing
        throw = self.robot.throw_rock()
        if throw[0]:
            self.rocks.append(throw[1])

        # Alien moving including climbing
        climbing_index = 0
        for alien in self.aliens:
            index = 0
            # Alien climbing controls
            if not self.alien_climbing[climbing_index]:
                stairs_list = self.stairs.copy()
                for stairs in stairs_list[0:-1]:
                    for stair in stairs:
                        if alien.is_at_stair(stair, index):
                            self.alien_climbing[climbing_index] = random.choice([True, False])
                    index += 1
            if self.alien_climbing[climbing_index]:
                alien.climb_up()
                if alien.is_alien_at_the_top_of_stair(self.stairs):
                        self.alien_climbing[climbing_index] = False
            # alien walking
            if (not self.alien_climbing[climbing_index]) and (not self.is_not_on_platform(alien)):
                if alien.is_alien_moving_right():
                    if alien.is_walking_right():
                        self.isStepUp("right", alien)
                    else:
                        alien.right = False
                elif not alien.is_alien_moving_right():
                    if alien.is_walking_left():
                        self.isStepUp("left", alien)
                    else:
                        alien.right = True
            climbing_index += 1

        # Alien Deploying
        deploy = self.spaceship.deploy_alien()
        if deploy[0] and len(self.aliens) <= 20:
            self.aliens.append(deploy[1])
            self.alien_climbing.append(False)

    # Falling of rocks and aliens
    def object_falling(self):
        for rock in self.rocks:
            if self.is_not_on_platform(rock):
                rock.fall()
        for alien in self.aliens:
            if self.is_not_on_platform(alien):
                alien.fall()
        if self.is_not_on_platform(self.player):
            self.player.fall()

    # On platform check for mainly falling methods of player and rocks
    def is_not_on_platform(self, who):
        for platforms in self.platforms:
            for platform in platforms:
                if who.is_on_platform(platform):
                    return False
        return True
    
    def jump(self):
        self.player.jump()

    # Cumulative rendering method for static obstacle objects to call in the tick method in Game object
    # Static and animated object rendering is not done in the same method to avoid rendering animated objects before starting the game.
    def draw_obstacles(self, screen):
        for floor in self.platforms:
            for platform in floor:
                platform.draw(screen)
        for stairs in self.stairs:
            for stair in stairs:
                stair.draw(screen)

    # Removal of excess rocks
    def remove_fallen_rocks(self):
        if len(self.rocks) != 0:
            if self.rocks[0].is_fallen():
                self.rocks.pop(0)

    # Game over check
    def game_over(self):
        # check rocks
        for rock in self.rocks:
            if self.player.did_hit_rock(rock):
                return True
        # check aliens
        for alien in self.aliens:
            if self.player.did_hit_alien(alien):
                return True
        # check if the player fell down
        if self.player.did_fall():
            return True
        return False
    
    # game won
    def you_won(self):
        return self.player.did_collide_with_spacebro(self.spacebro)
    
    # Calculate score
    def score_calculation(self, tick):
        if tick % 48:
            self.score += 3

    # Render score 
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