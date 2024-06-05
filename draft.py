from flask import Flask, render_template, request, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = 'FALKFAskfmakfjakfa2282282$##'

boggle_game = Boggle()


"""
DISPLAYING THE BOARD

1- The first thing you need to do is display the board in a Jinja template.
    - You will be generating a board on the backend using a function from the "boggle.py" file and sending that to your Jinja template.
    - Using Jinja, display the board on the page.
2- Since you will also be using this board in other routes, make sure to place it in the session.
3-  Once you have displayed the board --> add a form that allows a user to submit a guess.
"""

@app.route('/')
def homepage():
    """Display board and add form for user to submit a guess."""

    board = boggle_game.make_board()
    session['board'] = board

    return render_template('board.html', board=board)
