from flask import Flask, render_template, request, session, jsonify
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = 'FALKFAskfmakfjakfa2282282$##'

boggle_game = Boggle()

#Store the current game score and the number of times played on the server side.
# Homepage route
@app.route('/')
def homepage():
    """Display board and add form for user to submit a guess."""

    board = boggle_game.make_board()
    session['board'] = board

    return render_template('board.html', board=board)

# Initialize the game: number of plays and highest score to 0
@app.before_request # Executes code before every request
def initialize_game():
    # Set conditions for both numb of plays and highest score and save them in session
    if 'numb_plays' not in session:
        session['numb_plays'] = 0
    if 'highest_score' not in session:
        session['highest_score'] = 0

# Update number of plays and highscore
@app.route('/update-stats', methods=['POST'])
def update_stats():
    # Retrieve data from form and initial score
    data = request.form
    score = int(data.get('score', 0))

    print(f"Received score: {score}")
    print(f"Session before update: {session}")

    # Increment numb of plays in session
    session['numb_plays'] += 1

    # Set condition in case score is higher than highest score in session
    if score > session['highest_score']:
        session['highest_score'] = score
    
    print(f"Session after update: {session}")
    
    # Return json dict for number of plays and highscore in session
    return jsonify({
        'numb_plays': session['numb_plays'], 
        'highest_score': session['highest_score']
        })

@app.route('/check-word', methods=['POST'])
def get_word():
    word = request.json['word']
    board = session.get('board', [])
    submitted_words = session.get('submitted_words', [])
    
    print(f"Received word: {word}")
    print(f"Board: {board}")
    print(f"Already submitted words: {submitted_words}")

    if word in submitted_words:
        response = {"result": "already-submitted"}
    else:
        result = boggle_game.check_valid_word(board, word)
        if result == "ok":
            submitted_words.append(word)
            session['submitted_words'] = submitted_words
            response = {"result": "ok"}
        elif result == "not-on-board":
            response = {"result": "not-on-board"}
        else:
            response = {"result": "not-a-word"}
    
    return jsonify(response)




 