from constant import Colour, n_COL, n_ROW, WIDTH, HEIGHT, Position
import pygame


class Game:
    def __init__(self) -> None:
        pass

    def show_background(self, surface):
        for row in range(n_ROW):
            for col in range(n_COL):
                if (row+col) % 2:
                    colour = Colour.DARK_BLUE
                else:
                    colour = Colour.LIGHT_BLUE
                square_SIZE = WIDTH/n_ROW
                rect = (col*square_SIZE, row*square_SIZE,
                        square_SIZE, square_SIZE)
                pygame.draw.rect(surface, colour, rect)
