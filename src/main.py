from Game import Game
import pygame as pg

game = Game()

pg.init()
screen = pg.display.set_mode((960, 720))
clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    screen.fill("gray23")

    game.tick(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()