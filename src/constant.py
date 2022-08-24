# Board Information
from types import SimpleNamespace


WIDTH = 950
HEIGHT = 950
n_ROW = 8
n_COL = 8


Colour = SimpleNamespace()
Colour.BLACK = (0, 0, 0)
Colour.WHITE = (255, 255, 255)
Colour.DARK_BLUE = (15, 15, 50)
Colour.LIGHT_BLUE = (100, 100, 245)
Colour.DARK_GREEN = (0, 0, 0)
Colour.LIGHT_GREEN = (0, 0, 0)


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


TEAM = SimpleNamespace()
TEAM.MY_TEAM = 1
TEAM.OPPONENT_TEAM = -1


# my_choice = choose_team()
# if my_choice == 'Black':
TEAM.WHITE = TEAM.OPPONENT_TEAM
TEAM.BLACK = TEAM.MY_TEAM
# else:
#     TEAM.WHITE = TEAM.OPPONENT_TEAM
#     TEAM.BLACK = TEAM.MY_TEAM

Cost = SimpleNamespace()
Cost.PAWN = 1.0
Cost.ΚΝΙΓΗΤ = 3.0
Cost.BISHOP = 3.1
Cost.ROOK = 6.0
Cost.QUEEN = 15.0
Cost.KING = 1000.0
