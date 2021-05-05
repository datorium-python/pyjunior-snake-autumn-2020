import pygame
import constants

class Snake:

    rectangle_size = 20

    def __init__(self, x, y):

        self.rectangle_list = []
        first_rectangle = pygame.Rect(
            x,
            y,    
            Snake.rectangle_size,
            Snake.rectangle_size,
        )
        self.rectangle_list.append(first_rectangle)

        self.length = 1
        self.x_change = 0
        self.y_change = 0

    def get_first_rectangle(self):

        first_rectangle = self.rectangle_list[-1]
        return first_rectangle

    def draw_snake(self, window):

        for rectangle in self.rectangle_list[:-1]:
            pygame.draw.rect(window, constants.FOREST_GREEN, rectangle)

        first_rectangle = self.get_first_rectangle()
        pygame.draw.rect(window, constants.GREEN, first_rectangle)

    def move_snake(self):
        """
        Adds a new segmen to the list, if there are more rectangles
        than snake length, the oldes rectangle (first in the list)
        is deleted.
        """

        last_x = self.rectangle_list[-1].left
        last_y = self.rectangle_list[-1].top

        new_rectangle = pygame.Rect(
            last_x + self.x_change,
            last_y + self.y_change,
            Snake.rectangle_size,
            Snake.rectangle_size,        
        )
        self.rectangle_list.append(new_rectangle)

        if len(self.rectangle_list) > self.length:
            self.rectangle_list.pop(0)

    def is_crossing_itself(self):
        
        first_rectangle = self.get_first_rectangle()
        
        if first_rectangle.collidelist(self.rectangle_list[:-1]) == -1:
            return False
        
        return True

    def is_out_border(self, window):

        first_rectangle = self.get_first_rectangle()
        window_rectangle = window.get_rect()

        return not window_rectangle.contains(first_rectangle)


class Apple:

    size = 15

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_apple(self, window):

        rectangle = (
            self.x,
            self.y,
            Apple.size,
            Apple.size,
        )

        pygame.draw.rect(window, constants.RED, rectangle)

    def is_eaten(self, rectangle):

        apple_rect = pygame.Rect(
            self.x,
            self.y,
            Apple.size,
            Apple.size,
        )

        return apple_rect.colliderect(rectangle)