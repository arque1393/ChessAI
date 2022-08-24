from constant import Colour, n_COL, n_ROW, WIDTH, HEIGHT, Position
import pygame


class GameBackground:
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


class Square:
    def __init__(self, position, piece) -> None:
        self.position = position
        self.piece = piece


class GameBoard:
    def __init__(self) -> None:
        self.square = []

    def _create(self):
        self.square = [[Position(i, j) for i in range(n_ROW)]
                       for j in range(n_COL)]

    def _add_pieces(self):
        pass
