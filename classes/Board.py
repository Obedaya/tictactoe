class Board:
    _field = list(list())

    def __init__(self):
        self._field = [[" "] * 3 for i in range(3)]

    def make_move(self, move, token):
        x, y = move
        self._field[x][y] = token

    def is_valid_move(self, move):
        x, y = move
        if self._field[x][y] == " ":
            return True
        else:
            return False

    def get_field(self):
        return self._field

    def set_field(self, field):
        self._field = field
