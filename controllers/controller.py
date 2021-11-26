from flask import render_template
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title = "Home")

@app.route('/<choice_1>/<choice_2>')
def play_round(choice_1,choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game()
    winner = game.play_game(player_1, player_2)
    return render_template('result.html', title = "Result", winner = winner, player_1 = player_1, player_2 = player_2)