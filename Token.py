class Token:
    player = None
    token_type = None

    def __init__(self, player, token_type):
        self.player = player
        self.token_type = token_type

    def __eq__(self, other):
        return self.token_type == other.token_type
