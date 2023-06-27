class View:
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
        print("Press Enter to start the game.")
        start_input = input()
        field_start = """
             1 | 2 | 3
            ---+---+---
             4 | 5 | 6
            ---+---+---
             7 | 8 | 9 
            """
        print(field_start)
        test_2.get_input(tictactoe)
#        return field

    def get_input_playername(self, num):
        return input(f"Please enter name for player {num}: ")

    def get_input(self, move):
        move = (0, 0)
        ttt_input = int(input("Pick a number between 1 and 9: "))
        move = divmod(ttt_input - 1, 3)
        print(move)
        return move

    def print_field(self):
        field = """
            {} | {} | {}
           ---+---+---
            {} | {} | {}
           ---+---+---
            {} | {} | {}
           """

        # Create a list of placeholders for the cell values
        placeholders = []
        for i in tictactoe:
            placeholders.extend([str(j) if j != 0 else ' ' for j in i])
        # Fill in the placeholders in the field string with the cell values
        field = field.format(*placeholders)