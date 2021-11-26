from types import resolve_bases
import unittest

from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_rock = Player("Player1", "rock")
        self.player_paper = Player("Player2", "paper")
        self.player_scissors = Player("Player3", "scissors")
        self.game = Game()
    
    def test_game_rock_beats_scissors(self):
        result = self.game.play_game(self.player_rock, self.player_scissors)
        self.assertEqual(self.player_rock, result)
    
    def test_game_rock_loses_against_paper(self):
        result = self.game.play_game(self.player_rock, self.player_paper)
        self.assertEqual(self.player_paper, result)
    
    def test_game_scissors_beats_paper(self):
        result = self.game.play_game(self.player_scissors, self.player_paper)
        self.assertEqual(self.player_scissors, result)
    
    def test_game_scissors_loses_against_rock(self):
        result = self.game.play_game(self.player_scissors, self.player_rock)
        self.assertEqual(self.player_rock, result)
    
    def test_game_paper_beats_rock(self):
        result = self.game.play_game(self.player_paper, self.player_rock)
        self.assertEqual(self.player_paper, result)
    
    def test_game_paper_loses_against_scisors(self):
        result = self.game.play_game(self.player_paper, self.player_scissors)
        self.assertEqual(self.player_scissors, result)
    
    def test_game_return_none_on_tie(self):
        result = self.game.play_game(self.player_rock, self.player_rock)
        self.assertEqual(None, result)
