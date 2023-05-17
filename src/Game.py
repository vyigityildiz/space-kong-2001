from Level import Level
import pygame as pg

class Game():
    def __init__(self) -> None:
        pass

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

    def tick():
        pg.init()
        screen = pg.display.set_mode((960, 720))
        clock = pg.time.Clock()
        running = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            screen.fill("blue")

            pg.display.flip()
            clock.tick(60)

        pg.quit()

    def _set_tick_speed(self):
        pass
