from typing import Literal
from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_required, current_user
import random
import SQL_db

games = Blueprint('games', __name__)

@games.route("/hangman", methods=["GET", "POST"])
@login_required
def hangman():
    db = SQL_db.Hangman()
    db.connect_db()
    db.create_table()
    # db.clear_table()
    # GET method
    if request.method == "GET":
        if db.check_id(current_user.get_id()):
            with open("./text documents/hangman-wordlist.txt") as read:
                words = list(map(str, read))
                chosen_word = random.choice(words)
                chosen_word = chosen_word.upper()
                guess_word = len(chosen_word) * "_ "
            db.insert_data(current_user.get_id(), chosen_word)
            db.commit_db()
            return render_template("hangman.html", word = guess_word)
        else:
            chosen_word = db.retrieve_word(current_user.get_id())
            guess_word = len(chosen_word) * "_ "
            return render_template("hangman.html", word = guess_word)

    # POST method
    if request.method == "POST":
        guess_letter = request.get_data(as_text=Literal[True]).strip('"')
        if db.retrieve_guesses(current_user.get_id()) == None:
            db.update_guesses(guess_letter, current_user.get_id())
            db.commit_db()
        else:
            guesses = db.retrieve_guesses(current_user.get_id())
            # guess_list = list(map(str, guess_list))
            # guess_list.append(guess_letter.strip('"'))
            guesses = "".join((guesses, guess_letter))
            db.update_guesses(guesses, current_user.get_id())
            db.commit_db()
        return render_template("hangman.html")
    
        # if not guess_letter:
        #     flash("Make a valid guess", category="error")
        # else:
        #     flash("Valid :D", category="success")
    db.close_db()

@games.route('/madlibs')
def madlibs():
    return render_template("madlibs.html")

@games.route('/rps')
def rps():
    return render_template("rockpaperscissors.html")