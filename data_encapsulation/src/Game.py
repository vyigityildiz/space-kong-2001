from Level import Level
import pygame as pg

class Game():
    def __init__(self) -> None:
        self.level = Level()
        self.started = False
        self.score = 0
        self.pressed_right = False
        self.pressed_left = False
        self.pressed_up = False
        self.jumping = False
        self.game_over = False
        self.won = False

    def climb_down(self):
        self.level.isNearStairs("down", self.level.player)

    def climb_up(self):
        self.level.isNearStairs("up", self.level.player)

    def jump(self):
        self.jumping = True

    def move_left(self):
        self.level.isStepUp("left", self.level.player)

    def move_right(self):
        self.level.isStepUp("right", self.level.player)

    def pause():
        pass

    def displayPause(self):
        pass

    def removePauseDisplay(self):
        pass

    def resume(self):
        pass

    def start(self):
        self.started = True

    def tick(self, screen, frame, events, tick):
        for event in events:
            # Starting the game by pressing any key
            if event.type == pg.KEYDOWN:
                if not self.started:
                    self.start()
                # Key press control checks        
                if event.key == pg.K_LEFT:
                    self.pressed_left = True
                elif event.key == pg.K_RIGHT:
                    self.pressed_right = True
                elif event.key == pg.K_UP:
                    self.pressed_up = True
                elif event.key == pg.K_DOWN:
                    self.climb_down()
                if event.key == pg.K_SPACE:
                    if not self.level.is_not_on_platform(self.level.player):
                        self.jump_tick = tick
                        self.jump()
            # Key up control checks
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.pressed_left = False
                elif event.key == pg.K_RIGHT:
                    self.pressed_right = False
                elif event.key == pg.K_UP:
                    self.pressed_up = False

        # Displaying the starting text
        if not self.started:
            pg.font.init()
            font_to_use = pg.font.SysFont('arial', 50)
            text_surface = font_to_use.render('Press any key to start.', False, (255, 255, 255))
            screen.blit(text_surface, (0,0))

        # Checking if the player is in the air if True then player falls
        if self.level.is_not_on_platform(self.level.player):
            self.level.player.fall()
        
        # Objects fall control
        self.level.object_falling()

        # Moving, jumping is handled in the event loop TODO: bug fix climb down
        if self.pressed_right:
            self.move_right()
        if self.pressed_left:
            self.move_left()
        if self.pressed_up and not self.jumping:
            self.climb_up()
        if self.jumping:
            self.level.player.jump()
            if tick - self.jump_tick == 58:
                self.jumping = False
        
        if self.started:
            self.level.control_moving_instances()
        
        # Removing excess rocks
        self.level.remove_fallen_rocks()

        # Score calculation and render
        if not self.won and self.started and not self.game_over:
            self.level.score_calculation(tick)
        
        if self.started and not self.game_over:
            self.level.write_score(screen)

        # Game Over controller
        if not self.game_over:
            self.game_over = self.level.game_over()

        if self.game_over and not self.won:
            pg.font.init()
            font_to_use = pg.font.SysFont('arial', 50)
            text_surface = font_to_use.render('Game Over You Lose :(', False, (255, 255, 255))
            screen.blit(text_surface, (0,0))
        
        # Game winning controller
        if not self.won:
            self.won = self.level.you_won()
        
        if self.won:
            pg.font.init()
            font_to_use = pg.font.SysFont('arial', 50)
            text_surface = font_to_use.render('You Win :)', False, (255, 255, 255))
            screen.blit(text_surface, (0,0))

        # Rendering
        self.level.draw_obstacles(screen)
        if self.started and not self.game_over and not self.won:
            self.level.draw_animated_instances(screen, frame)

    def _set_tick_speed(self):
        pass
