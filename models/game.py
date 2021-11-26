class Game():
    def __init__(self):
        self._win_conditions = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
    
    def play_game(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return None
        elif player_2.choice == self._win_conditions[player_1.choice]:
            return player_1
        else:
            return player_2