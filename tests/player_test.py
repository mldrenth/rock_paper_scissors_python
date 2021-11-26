import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Frodo", "scissors")
    
    def test_player_has_name(self):
        self.assertEqual("Frodo", self.player.name)
    
    def test_player_has_choice(self):
        self.assertEqual("scissors", self.player.choice)