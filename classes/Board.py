import copy


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

    def __copy__(self):
        new_board = Board()  # Create a new instance of the Board class
        new_board._field = copy.copy(self._field)  # Shallow copy the field
        new_board._last_move = self._last_move
        return new_board

    def __deepcopy__(self, memo):
        new_board = Board()  # Create a new instance of the Board class
        new_board._field = copy.deepcopy(self._field, memo)  # Deep copy the field
        new_board._last_move = copy.deepcopy(self._last_move, memo)
        return new_board

