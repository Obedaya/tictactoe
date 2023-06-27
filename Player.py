class Player:
    _name = None
    _type = None

    def __init__(self, name, player_type):
        self._name = name
        self._type = player_type

    def get_type(self):
        return self._type