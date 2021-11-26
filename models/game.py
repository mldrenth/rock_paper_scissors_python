from models.player import Player
import random

class Game():
    def __init__(self):
        self._win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
    
    def create_computer_player(self):
        choices = ["rock", "paper", "scissors"]
        return Player("Computer", random.choice(choices))
    
    def play_game(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return None
        elif player_2.choice == self._win_conditions[player_1.choice]:
            return player_1
        else:
            return player_2