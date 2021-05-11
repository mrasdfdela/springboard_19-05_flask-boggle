from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)
# app.debug = True

GAME = Boggle()

@app.route('/')
def home_page():
    # boggle_game = Boggle()
    board = GAME.make_board()
    session['board'] = board
    return render_template("index.html", board=session['board'])


@app.route('/', methods=['POST'])
def submit_word():
    req = request.get_json()
    params = req['params']
    new_word = params['search_word']

    board = session['board']
    result = GAME.check_valid_word(board, new_word)

    return jsonify({'result': result})