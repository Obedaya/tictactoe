# Handles all the Data and logical components
class Model:
    field = list(list())

    def __init__(self):
        self.field = self.create_field()

    def create_field(self):
        field = [[None] * 3 for i in range(3)]
        return field

    def make_move(self, move, player):
        x, y = move
        if player == "x":
            self.field[x][y] = 'x'
        elif player == "o":
            self.field[x][y] = 'o'

    def get_field(self):
        return self.field

# Handles the connection between Model and View
class Controller:

    def is_valid_move(self, field, move):
        x, y = move
        if field[x][y] == 'x' or field[x][y] == 'o':
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

    def round(self, model, view, player, round):
        field = model.get_field()
        view.print_field(field)
        move = view.get_input()
        if self.is_valid_move(field, move):
            field = model.make_move(move, player)
            view.print_field(field)
        else:
            view.not_valid_move()
        if round == 5 and self.is_win(field):
            self.end_game(view)

    def end_game(self, view):
        view.print_end_game()
        view.get_input()





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
