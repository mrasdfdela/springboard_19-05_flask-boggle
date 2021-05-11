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
    """ initialize boggle game & board """
    board = GAME.make_board()
    session['board'] = board
    return render_template("index.html", board=session['board'])


@app.route('/', methods=['POST'])
def submit_word():
    """ receive word request and evaluate validity """
    req = request.get_json()
    params = req['params']
    new_word = params['search_word']

    curr_responses = session['responses']

    if new_word not in curr_responses:
        curr_responses.append(new_word)
        session['responses'] = curr_responses
        result = GAME.check_valid_word(session['board'], new_word)
        return jsonify({'result': result})
    else:
        return jsonify({'result':''})


@app.route('/score_board',methods=['POST'])
def submit_score():
  """ after game expires, update high score in session """
  req = request.get_json()
  params = req["params"]
  high_score = session.get('high_score',0)
  if params['new_score'] > high_score:
    session['high_score'] = params['new_score']

  return jsonify({'high_score': session['high_score']})
