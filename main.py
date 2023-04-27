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

    def is_win(self, field):
        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            return field[1][1]
        for i in range(3):
            if field[i][0] == field[i][1] == field[i][2] or field[0][i] == field[1][i] == field[2][i]:
                return field[i][i]


test = Model()
print(test.create_field())
tictactoe = [['y', 'y', 0], ['x', 'y', 'y'], ['y', 0, 'y']]
print(test.is_win(tictactoe))
print("Hello World")
