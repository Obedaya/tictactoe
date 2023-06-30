import pickle
import os
from classes import Game as g


class FileHandler:

    def save_game_state(self, file_path, game_state):
        with open("data/savegames/" + file_path, 'wb') as file:
            pickle.dump(game_state, file)

    def load_game_state(self, file_path):
        try:
            with open("data/savegames/" + file_path, 'rb') as file:
                game_state = pickle.load(file)
                print(game_state)
                if not isinstance(game_state, g.Game):
                    raise TypeError("Invalid game state format")
        except FileNotFoundError:
            raise FileNotFoundError("Game state file not found")
        except pickle.UnpicklingError:
            raise TypeError("Failed to load game state")

        return game_state

    def get_list_savegames(self):
        savegames_list = []
        for filename in os.listdir("data/savegames/"):
            if os.path.isfile(os.path.join("data/savegames/", filename)):
                savegames_list.append(filename)
        return savegames_list
