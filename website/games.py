from typing import Literal
from flask import Blueprint, render_template, request, jsonify, flash, redirect
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
        # checks if the user has a word tied to their account - if they do not, a new word is assigned
        if db.check_id(current_user.get_id()):
            with open("./text documents/hangman-wordlist.txt") as read:
                words = list(map(str, read))
                chosen_word = random.choice(words).strip("\n")
                chosen_word = chosen_word.upper()
                guess_word = len(chosen_word) * "_ "
            db.insert_data(current_user.get_id(), chosen_word)
            db.commit_db()
            return render_template("hangman.html", word = guess_word)
        # if user already exists in data base this retrieves the word and sends it to the client
        else:
            chosen_word = db.retrieve_word(current_user.get_id())
            guesses = db.retrieve_guesses(current_user.get_id())
            # guess_letter = request.get_data(as_text=Literal[True]).strip('"')
            # once I reset the database can remove the strip function under
            guess_word = (len(chosen_word.strip("\n"))) * "_ "
            return render_template("hangman.html", word = guess_word)

    # PUT method

    # POST method
    if request.method == "POST":
        guess_letter = request.get_data(as_text=Literal[True]).strip('"')
        turns = 6
        guesses = db.retrieve_guesses(current_user.get_id())
        if guesses == None:
            db.update_data(guess_letter, turns, current_user.get_id())
            db.commit_db()
        else:
            if guess_letter not in guesses:
                guesses = "".join((guesses, guess_letter))
                # guess_list = list(map(str, guesses))
                db.update_data(guesses, turns, current_user.get_id())
                db.commit_db()
            else:
                print("This letter was already guessed")
        return game_state()
    db.close_db()

@games.route("hangman/api/gamestate")
@login_required
def game_state():
    db = SQL_db.Hangman()
    db.connect_db()
    # if not db.check_id(current_user.get_id()):
        # chosen_word = db.retrieve_word(current_user.get_id())
    guesses = db.retrieve_guesses(current_user.get_id())
    # guess_word = (len(chosen_word.strip("\n"))) * "_ "
    return jsonify(guesses = guesses)


@games.route('/madlibs')
def madlibs():
    return render_template("madlibs.html")

@games.route('/rps')
def rps():
    return render_template("rockpaperscissors.html")