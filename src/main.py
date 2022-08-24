import pygame
import sys
import numpy as np

from constant import *
from game import Game


class MainWindow:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Board")
        self.game_backgroun = Game()

    def main_loop(self):
        while True:
            self.game_backgroun.show_background(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # print(self.screen.get_height())
            # print(self.screen.get_width())
            pygame.display.update()


def choose_team():
    return input("please enter your team :").lower()


def main():
    window = MainWindow()
    window.main_loop()


if __name__ == '__main__':
    main()
