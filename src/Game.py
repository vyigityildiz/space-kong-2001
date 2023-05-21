from Level import Level
import pygame as pg

class Game():
    def __init__(self) -> None:
        self.level = Level()
        self.started = False
        self.score = 0
        self.pressed_right = False
        self.pressed_left = False
        self.pressed_down = False
        self.pressed_up = False

    def climb_down(self):
        pass

    def climb_up(self):
        pass

    def jump(self):
        pass

    def move_left(self):
        self.level.isStepUp("left")

    def move_right(self):
        self.level.isStepUp("right")

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

    def render(self):
        pass

    def tick(self, screen, frame, events):
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
                    self.pressed_down = True
                if event.key == pg.K_SPACE: # TODO: Change after programming the jump method
                    self.jump()
            # Key up control checks
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.pressed_left = False
                elif event.key == pg.K_RIGHT:
                    self.pressed_right = False
                elif event.key == pg.K_UP:
                    self.pressed_up = False
                elif event.key == pg.K_DOWN:
                    self.pressed_down = False

        # Displaying the starting text
        if not self.started:
            pg.font.init()
            font_to_use = pg.font.SysFont('arial', 50)
            text_surface = font_to_use.render('Press any key to start.', False, (255, 255, 255))
            screen.blit(text_surface, (0,0))

        # Checking if the player is in the air if True then player falls
        if self.level.is_player_not_on_platform():
            self.level.player.fall()

        # Moving TODO: Complete for stairs
        if self.pressed_right:
            self.move_right()
        if self.pressed_left:
            self.move_left()

        # Rendering
        self.level.draw_obstacles(screen)
        if self.started:
            self.level.draw_animated_instances(screen, frame)

    def _set_tick_speed(self):
        pass
