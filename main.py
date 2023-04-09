import pygame as pg

from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

get_random_pos = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0,0,TILE_SIZE - 2, TILE_SIZE -2])
snake.center = get_random_pos()

food = snake.copy()
food.center = get_random_pos()

length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time = 0 
time_step = 300
screen = pg.display.set_mode((WINDOW, WINDOW))
clock = pg.time.Clock()

up_direction = (0, -1 * TILE_SIZE)
down_direction = (0, TILE_SIZE)
left_direction = (-1 * TILE_SIZE, 0)
right_direction = (TILE_SIZE, 0)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and snake_dir != down_direction:
                snake_dir = up_direction
            if event.key == pg.K_s and snake_dir != up_direction:
                snake_dir = down_direction
            if event.key == pg.K_a and snake_dir != right_direction:
                snake_dir = left_direction
            if event.key == pg.K_d and snake_dir != left_direction:
                snake_dir = right_direction
            
    screen.fill('black')
    
    #borders and eat itself 
    eat_self = pg.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or eat_self:
        snake.center = get_random_pos()
        food.center = get_random_pos()
        length = 1
        snake_dir = (0, 0)
        segments = snake.copy
    
    # if we catch the food?
    if(snake.center == food.center):
        food.center = get_random_pos()
        length += 1
    
    #draw food
    pg.draw.rect(screen, 'red', food)    
    #draw snake
    for segment in segments:
        pg.draw.rect(screen, 'green', segment)
    #snake moove
    time_now = pg.time.get_ticks()
    if(time_now - time > time_step):
        time  = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    pg.display.flip()
    clock.tick(60)


