from typing import Literal
from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_required, current_user
import random
import SQL_db

games = Blueprint('games', __name__)

@games.route("/hangman", methods=["GET", "POST"])
@login_required
def hangman():
    # GET method
    if request.method == "GET":
        db = SQL_db.Hangman()
        db.connect_db()
        db.create_table()
        if db.check_id(current_user.get_id()):
            with open("./text documents/hangman-wordlist.txt") as read:
                words = list(map(str, read))
                chosen_word = random.choice(words)
                chosen_word = chosen_word.upper()
                guess_word = len(chosen_word) * "_ "
            db.insert_data(current_user.get_id(), chosen_word)
            return render_template("hangman.html", word = guess_word)
        else:
            chosen_word = db.get_word(current_user.get_id())
            guess_word = len(chosen_word) * "_ "
            return render_template("hangman.html", word = guess_word)
    db.close_db()
        # return render_template("hangman.html")
    # POST method
    if request.method == "POST":
        guess_letter = request.get_data(as_text=Literal[True])
        print(guess_letter)
        # for x in range(8):
        #     print(guess_letter + str(x))
            # if guess_letter == chosen_word[index] and 
            # if guess_letter == letter:
            #     print("Horray!")

        return render_template("hangman.html")
        
        # if not guess_letter:
        #     flash("Make a valid guess", category="error")
        # else:
        #     flash("Valid :D", category="success")

@games.route('/madlibs')
def madlibs():
    return render_template("madlibs.html")

@games.route('/rps')
def rps():
    return render_template("rockpaperscissors.html")