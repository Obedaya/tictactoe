class Board:
    _field = list(list())

    def __init__(self):
        self._field = [[None] * 3 for i in range(3)]

    def make_move(self, move, token):
        x, y = move
        self._field[x][y] = token

    def get_field(self):
        return self._field
