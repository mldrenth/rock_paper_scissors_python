import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        player_rock = Player("Player1", "rock")
        player_paper = Player("Player2", "paper")
        player_scissors = Player("Player3", "scissors")
