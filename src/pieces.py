from constant import Team, Cost


class Piece:
    def __init__(self, name: str, team: tuple, cost: float,
                 texture=None, texture_rect=None) -> None:
        self.name = name
        self.Team = team
        self.cost = cost
        self.texture = texture
        self.texture_rect = texture_rect


class Pawn(Piece):
    def __init__(self, team):
        self.direction = -1 if team == Team.WHITE else 1
        super().__init__("Pawn", team, Cost.PAWN)


class Knight(Piece):
    def __init__(self, team):
        super().__init__("Knight", team, Cost.KNIGHT)


class Bishop(Piece):
    def __init__(self, team):
        super().__init__("Bishop", team, Cost.BISHOP)


class Rook(Piece):
    def __init__(self, team):
        super().__init__("Rook", team, Cost.ROOK)


class Queen(Piece):
    def __init__(self, team):
        super().__init__("Queen", team, Cost.QUEEN)


class King(Piece):
    def __init__(self, team):
        super().__init__("King", team, Cost.KING)
