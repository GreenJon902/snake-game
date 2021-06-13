import sys

import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE

from static_vars import *

pygame.init()

DISPLAY = pygame.display.set_mode(window_size, 0, 32)

snake_pos = initial_snake_pos
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


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        draw()