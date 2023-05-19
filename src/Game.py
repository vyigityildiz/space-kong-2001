from Level import Level
import pygame as pg

class Game():
    def __init__(self) -> None:
        self.level = Level()

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
        pass

    def render(self):
        pass

    def tick(self, screen, frame):
        self.level.draw_obstacles(screen)
        self.level.draw_animated_instances(screen, frame)

    def _set_tick_speed(self):
        pass
