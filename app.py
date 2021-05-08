from boggle import Boggle
from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)
# app.debug = True

boggle_game = Boggle()

@app.route('/')
def home_page():
    return '<h1>Hello world!</h1>'
