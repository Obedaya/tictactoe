class Model:
    def create_field(self):
        return [[0] * 3 for i in range(3)]

    def make_move(self, move, field, player):
        x, y = move
        if player == "x":
            field[x][y] = 1
        elif player == "o":
            field[x][y] = 0

    def is_valid_move(self, field, move):
        x, y = move
        if field[x][y] == 1 or field[x][y] == 0:
            return False
        else:
            return True

    def is_win(self, field, player):
        for i in range(3):
            if all(x == field[i][0] for x in field):
                return field[i][0]
        for i in range(3):
            if all(x == field[0][i] for x in field):
                return field[0][i]


test = Model()
print(test.create_field())
print("Hello World")
