class Board:
    _field = list(list())
    _last_move = None

    def __init__(self):
        self._field = [[" "] * 3 for i in range(3)]

    def make_move(self, move, token):
        x, y = move
        self._field[x][y] = token
        self._last_move = move

    def get_field(self):
        return self._field

    def undo(self):
        x, y = self._last_move
        self._field[x][y] = " "
