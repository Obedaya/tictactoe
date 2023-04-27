# Handles all the Data and logical components
class Model:
    def create_field(self):
        return [[0] * 3 for i in range(3)]

    def make_move(self, move, field, player):
        x, y = move
        if player == "x":
            field[x][y] = 1
        elif player == "o":
            field[x][y] = 0


# Handles the connection between Model and View
class Controller:

    def is_valid_move(self, field, move):
        x, y = move
        if field[x][y] == 'x' or field[x][y] == 'y':
            return False
        else:
            return True

    def is_win(self, field):
        # Check for diagonal win
        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            return field[1][1]
        # Check for vertical or horizontal win
        for i in range(3):
            if field[i][0] == field[i][1] == field[i][2] or field[0][i] == field[1][i] == field[2][i]:
                return field[i][i]
        # Check for tie
        if all(all(row) for row in field):
            return "tie"
        # No winner yet
        return None


# Handles the View and User Input
class View:
    placeholder = None


# Handles the View, Model and Controller
class GameManager:
    placeholder = None


test = Model()
print(test.create_field())
tictactoe = [['y', 'y', 0], ['x', 'y', 'y'], ['y', 0, 'y']]
print(test.is_win(tictactoe))
print("Hello World")
