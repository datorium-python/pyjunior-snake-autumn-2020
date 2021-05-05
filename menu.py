import pygame
import constants

pygame.init()
font = pygame.font.SysFont(constants.FONT_NAME, constants.MENU_FONT_SIZE)


def menu(window):

    window.fill(constants.BLACK)

    message = "PRESS ANY KEY TO PLAY"
    text = font.render(message, True, constants.WHITE)

    x = window.get_width() / 2 - text.get_width() / 2
    y = window.get_height() / 2 - text.get_height() / 2
    coordinates = (x, y)

    window.blit(text, coordinates)
    pygame.display.update()