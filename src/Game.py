from Level import Level
import pygame as pg

class Game():
    def __init__(self) -> None:
        self.level = Level()
        self.started = False

    def climb_down(self):
        pass

    def climb_up(self):
        pass

    def jump(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

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
            if event.type == pg.KEYDOWN:
                self.start()

        if not self.started:
            pg.font.init()
            font_to_use = pg.font.SysFont('arial', 50)
            text_surface = font_to_use.render('Press any key to start.', False, (255, 255, 255))
            screen.blit(text_surface, (0,0))

        self.level.draw_obstacles(screen)
        if self.started:
            self.level.draw_animated_instances(screen, frame)

    def _set_tick_speed(self):
        pass
