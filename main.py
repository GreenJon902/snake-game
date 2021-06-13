import random
import sys
import time

import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE, K_w, K_a, K_s, K_d

from static_vars import *

pygame.init()

DISPLAY = pygame.display.set_mode(window_size, 0, 32)
pygame.display.set_caption("Snake - GreenJon902")

snake_poses = initial_snake_poses
snake_direction = initial_snake_direction
food_pos = "no"


def draw():
    DISPLAY.fill(background_color)

    for sx in range(horizontal_square_amount):
        x = sx * square_size + sx * square_gap + square_gap

        for sy in range(vertical_square_amount):
            y = sy * square_size + sy * square_gap + square_gap

            pygame.draw.rect(DISPLAY, square_color, (x, y, square_size, square_size))


    pygame.draw.rect(DISPLAY, food_color, (food_pos[0] * square_size + food_pos[0] * square_gap + square_gap,
                                            food_pos[1] * square_size + food_pos[1] * square_gap + square_gap,
                                            square_size, square_size))


    for pos in snake_poses:
        pygame.draw.rect(DISPLAY, snake_color, (pos[0] * square_size + pos[0] * square_gap + square_gap,
                                                pos[1] * square_size + pos[1] * square_gap + square_gap,
                                                square_size, square_size))
    pygame.display.update()


def move_snake():
    global snake_poses
    new_pos = snake_poses[len(snake_poses) - 1].copy()

    new_pos[0] += snake_movement[snake_direction][0]
    new_pos[1] += snake_movement[snake_direction][1]

    if new_pos[0] < 0:
        new_pos[0] = horizontal_square_amount - 1
    elif new_pos[0] > horizontal_square_amount - 1:
        new_pos[0] = 0

    if new_pos[1] < 0:
        new_pos[1] = vertical_square_amount - 1
    elif new_pos[1] > vertical_square_amount - 1:
        new_pos[1] = 0

    snake_poses.pop(0)
    snake_poses.append(new_pos)

    for i, pos in enumerate(snake_poses):
        if pos == snake_poses[len(snake_poses) - 1] and i != len(snake_poses) - 1:
            print("Died at", pos)
            pygame.quit()
            sys.exit()


def check_food():
    global food_pos

    if food_pos == "no":
        food_pos = [random.randint(0, horizontal_square_amount - 1), random.randint(0, vertical_square_amount - 1)]

        print("Spawned food at", food_pos)

    if snake_poses[len(snake_poses) - 1] == food_pos:
        food_pos = [random.randint(0, horizontal_square_amount - 1), random.randint(0, vertical_square_amount - 1)]
        snake_poses.append(snake_poses[len(snake_poses) - 1])

        print("Spawned food at", food_pos)


update_timer = 0.0
time_before = time.time()
while True:
    time_after = time.time()
    update_timer += time_after - time_before

    if update_timer >= update_time:
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

        move_snake()
        update_timer = 0

    time_before = time.time()

    check_food()
    draw()
