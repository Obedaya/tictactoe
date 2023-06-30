from classes import Token as t

class View:
    def get_integer_input(self, message):
        while True:
            user_input = input(message)
            if user_input.isdigit():
                return int(user_input)
            elif user_input == 'q':
                return 'q'
            else:
                print("Invalid input. Please enter an integer.")

    def get_input_playername(self, num):
        return input(f"Please enter name for player {num}: ")

    def get_input_move(self):
        move = (0, 0)
        while True:
            ttt_input = self.get_integer_input("Pick a number between 1 and 9 or 'q' to save and quit: ")
            if ttt_input == 'q':
                return 'q'
            if 1 <= ttt_input <= 9:
                move = divmod(ttt_input - 1, 3)
                break
            else:
                print("Not a valid input!")
        return move

    def get_first_player(self, player1, player2):
        print("Who wants to start?")
        print(f"{player1.get_name()}: [1]")
        print(f"{player2.get_name()}: [2]")
        while True:
            player_input = self.get_integer_input("Choose a Player: ")
            if player_input == 1:
                return player1
            elif player_input == 2:
                return player2
            elif player_input == 'q':
                return 'q'
            else:
                print("This is not an valid option!")

    def get_input_file_path(self):
        return input("Please input the name of the file: ")

    def print_menu(self):
        print("Welcome to")
        intro = """
            ███      ▄█   ▄████████    ▄█   ▄█▄  ▄█       ▄██   ▄       ███      ▄██████▄     ▄████████ 
        ▀█████████▄ ███  ███    ███   ███ ▄███▀ ███       ███   ██▄ ▀█████████▄ ███    ███   ███    ███ 
           ▀███▀▀██ ███▌ ███    █▀    ███▐██▀   ███       ███▄▄▄███    ▀███▀▀██ ███    ███   ███    █▀  
            ███   ▀ ███▌ ███         ▄█████▀    ███       ▀▀▀▀▀▀███     ███   ▀ ███    ███  ▄███▄▄▄     
            ███     ███▌ ███        ▀▀█████▄    ███       ▄██   ███     ███     ███    ███ ▀▀███▀▀▀     
            ███     ███  ███    █▄    ███▐██▄   ███       ███   ███     ███     ███    ███   ███    █▄  
            ███     ███  ███    ███   ███ ▀███▄ ███▌    ▄ ███   ███     ███     ███    ███   ███    ███ 
           ▄████▀   █▀   ████████▀    ███   ▀█▀ █████▄▄██  ▀█████▀     ▄████▀    ▀██████▀    ██████████
        """
        print(intro)
        while True:
            print("----------------------------------")
            print("New game [1]")
            print("Load game [2]")
            print("Quit [3]")
            print("----------------------------------")
            option = self.get_integer_input("Choose an option: ")
            if option == 'q':
                option = 3
            if 1 <= option <= 3:
                return option
            else:
                print("Please choose a valid option!")

    def print_tutorial(self):
        field_start = """
             1 | 2 | 3
            ---+---+---
             4 | 5 | 6
            ---+---+---
             7 | 8 | 9
            """
        print("----------------------------------")
        print("The field is numbered from 1-9")
        print(field_start)
        print("At each move, select the corresponding index from the cell")
        print("Have fun with the game!")
        print("----------------------------------")

    def print_field(self, field):
        display_field = """
            {} | {} | {}
           ---+---+---
            {} | {} | {}
           ---+---+---
            {} | {} | {}
           """

        # Create a list of placeholders for the cell values
        placeholders = []
        for row in field:
            placeholders.extend([cell.token_type if isinstance(cell, t.Token) else ' ' for cell in row])

        # Fill in the placeholders in the display_field string with the cell values
        display_field = display_field.format(*placeholders)

        # Print the formatted field
        print(display_field)

    def print_nvm(self):
        print("This move is not valid!")

    def print_tie(self):
        print("The game is a tie!")

    def print_winner(self, winner):
        print("----------------------------------")
        print(f"Congratulations {winner} you won!")
        print("----------------------------------")

    def print_next_player(self, player):
        print(f"It's your turn: {player.get_name()}")

    def print_list_savegames(self, savegames_list):
        if savegames_list:
            for i in savegames_list:
                print("- " + i)

    def end(self):
        input("Thanks for playing! To go back to the menu press any button: ")
