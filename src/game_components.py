from constant import Colour, n_COL, n_ROW, WIDTH, HEIGHT, Position
import pygame
import numpy as np
from pieces import Piece, Pawn, Knight, Bishop, Rook, Queen, King


class Square:
    def __init__(self, position: Position, piece: Piece = None) -> None:
        self.position = position
        self.piece = piece


class GameBoard:
    def __init__(self) -> None:
        self.squares = None
        self._create()

    def _create(self):
        # self.square = [[Position(i, j) for i in range(n_ROW)]
        #                for j in range(n_COL)]
        self.squares = np.full((8, 8), Square(Position(0, 0)))
        for i in range(8):
            for j in range(8):
                self.squares[i, j] = Square(Position(i, j))

    def _add_pieces(self):
        pass
