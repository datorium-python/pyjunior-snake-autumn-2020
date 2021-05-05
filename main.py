import pygame
import constants
import game
import menu

pygame.init()

window = pygame.display.set_mode(constants.WINDOW_SIZE)
pygame.display.set_caption("Snake")


while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            game.game(window)

    menu.menu(window)
    