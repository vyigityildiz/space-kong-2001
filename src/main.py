from Game import Game
import pygame as pg

game = Game()

pg.init()
screen = pg.display.set_mode((960, 720))
clock = pg.time.Clock()
running = True

frame = 0
tick = 0
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
            
    screen.fill("gray6") # TODO: after done with level design change the color back to gray6

    game.tick(screen, frame, events)

    tick += 1
    if tick % 8 == 0:
        frame += 1

    pg.display.flip()
    clock.tick(24)

pg.quit()