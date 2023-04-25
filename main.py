class Model:
    def create_field(self):
        return [ [0]*3 for i in range(3)]

    def make_move(self, move, field, player):
        x, y = move
        if player == "x":
            field[x][y] = 1
        elif player == "o":
            field[x][y] = 0


test = Model()
print(test.create_field())
print("Hello World")

