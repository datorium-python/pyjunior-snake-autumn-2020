import pygame
import time
import random
import constants
from models import Snake, Apple

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE)


def draw_score(window, score):
    text = font.render(f"SCORE: {score}", True, constants.WHITE)
    coordinates = (10, 10)

    window.blit(text, coordinates)


def render(window, snake, apple, score):

    window.fill(constants.BLACK)
    
    snake.draw_snake(window)
    apple.draw_apple(window)
    draw_score(window, score)

    pygame.display.update()


def game(window):

    snake = Snake(
        x=random.randint(0, constants.WIDTH - Snake.rectangle_size),
        y=random.randint(0, constants.HEIGHT - Snake.rectangle_size)
    )

    apple = Apple(
        x=random.randint(0, constants.WIDTH - Apple.size),
        y=random.randint(0, constants.HEIGHT - Apple.size)
    )

    score = 0

    is_running = True
    while is_running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_running = False
                break

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:
                    snake.x_change = 0
                    snake.y_change = -snake.rectangle_size
                elif event.key == pygame.K_a:
                    snake.x_change = -snake.rectangle_size
                    snake.y_change = 0 
                elif event.key == pygame.K_s:
                    snake.x_change = 0
                    snake.y_change = snake.rectangle_size
                elif event.key == pygame.K_d:
                    snake.x_change = snake.rectangle_size
                    snake.y_change = 0

        snake.move_snake()

        if snake.is_crossing_itself() or snake.is_out_border(window):
            is_running = False

        head = snake.get_first_rectangle()
        if apple.is_eaten(head):
            snake.length += 1
            score += 1

            apple.x=random.randint(0, constants.WIDTH)
            apple.y=random.randint(0, constants.HEIGHT)

        render(window, snake, apple, score)
        clock.tick(constants.FPS)