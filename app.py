from boggle import Boggle
from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)
# app.debug = True


@app.route('/')
def home_page():
    boggle_game = Boggle()
    board = boggle_game.make_board()
    session['board'] = board
    return render_template("index.html", board=session['board'])
