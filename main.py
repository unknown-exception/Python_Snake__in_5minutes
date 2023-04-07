import pygame as pg

from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

get_random_pos = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0,0,TILE_SIZE - 2, TILE_SIZE -2])
snake.center = get_random_pos()
length = 1
segments = [snake.copy()]
screen = pg.display.set_mode((WINDOW, WINDOW))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    
    #draw snake
    for segment in segments:
        pg.draw.rect(screen, 'green', segment)

    pg.display.flip()
    clock.tick(60)
