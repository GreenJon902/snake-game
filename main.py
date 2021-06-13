import sys
import time

import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d

from static_vars import *

pygame.init()

DISPLAY = pygame.display.set_mode(window_size, 0, 32)

snake_pos = list(initial_snake_pos)
snake_direction = initial_snake_direction


def draw():
    DISPLAY.fill(background_color)

    for sx in range(horizontal_square_amount):
        x = sx * square_size + sx * square_gap + square_gap

        for sy in range(vertical_square_amount):
            y = sy * square_size + sy * square_gap + square_gap

            pygame.draw.rect(DISPLAY, square_color, (x, y, square_size, square_size))

    pygame.draw.rect(DISPLAY, snake_color, (snake_pos[0] * square_size + snake_pos[0] * square_gap + square_gap,
                                            snake_pos[1] * square_size + snake_pos[1] * square_gap + square_gap,
                                            square_size, square_size))

    pygame.display.update()


def move_snake():
    global snake_pos

    snake_pos[0] += snake_movement[snake_direction][0]
    snake_pos[1] += snake_movement[snake_direction][1]

    if snake_pos[0] < 0:
        snake_pos[0] = horizontal_square_amount - 1
    elif snake_pos[0] > horizontal_square_amount - 1:
        snake_pos[0] = 0

    if snake_pos[1] < 0:
        snake_pos[1] = vertical_square_amount - 1
    elif snake_pos[1] > vertical_square_amount - 1:
        snake_pos[1] = 0


snake_movement_timer = 0.0
time_before = time.time()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.key == K_w and snake_direction != "d":
                snake_direction = "u"
            elif event.key == K_a and snake_direction != "r":
                snake_direction = "l"
            elif event.key == K_s and snake_direction != "u":
                snake_direction = "d"
            elif event.key == K_d and snake_direction != "l":
                snake_direction = "r"


    time_after = time.time()
    snake_movement_timer += time_after - time_before
    if snake_movement_timer >= snake_movement_time:
        move_snake()
        snake_movement_timer = 0

    time_before = time.time()

    draw()
