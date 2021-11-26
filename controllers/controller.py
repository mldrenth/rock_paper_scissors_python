from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title = "Home")

@app.route('/play')
def play():
    return render_template('play_against_computer.html', title = "Play against Computer")

@app.route('/<choice_1>/<choice_2>')
def play_round(choice_1,choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    game = Game()
    winner = game.play_game(player_1, player_2)
    return render_template('result.html', title = "Result", winner = winner, player_1 = player_1, player_2 = player_2)

@app.route('/play', methods=["POST"])
def play_against_computer():
    game = Game()
    # Create human player from form
    player_name = request.form["name"]
    player_choice = request.form["options"]
    human_player = Player(player_name, player_choice)
    # Create computer player
    computer_player = game.create_computer_player()
    # Play a game and render
    winner = game.play_game(human_player, computer_player)
    return render_template('result.html', title = "Result", winner = winner, player_1 = human_player, player_2 = computer_player)