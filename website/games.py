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
    user = current_user.get_id()
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
            chosen_word = db.retrieve_word(user)
            guesses = db.retrieve_guesses(user)
            # once I reset the database can remove the strip function under
            guess_word = (len(chosen_word.strip("\n"))) * "_ "
            return render_template("hangman.html", word = guess_word)

    # POST method
    if request.method == "POST":
        turns = 6
        guess_letter = request.get_data(as_text=Literal[True]).strip('"')
        guesses = db.retrieve_guesses(user)
        chosen_word = db.retrieve_word(user)
        if guesses == None:
            if guess_letter not in chosen_word:
                turns -= 1
            db.update_data(guess_letter, turns, user)
            db.commit_db()
        else:
            if guess_letter not in guesses:
                guesses = ", ".join((guesses, guess_letter))
                if guess_letter not in chosen_word:
                    turns -= 1
                else:
                    turns = db.retrieve_turns(user)
            else:
                print("This letter was already guessed")
            db.update_data(guesses, turns, user)
            db.commit_db()
        return game_state()
    db.close_db()
   
@games.route("hangman/api/gamestate")
@login_required
def game_state():
    db = SQL_db.Hangman()
    db.connect_db()
    user = current_user.get_id()
    word = db.retrieve_word(user)
    guess_word = (len(word.strip("\n"))) * "_"
    guess_word = list(map(str, guess_word))
    guesses = db.retrieve_guesses(user)
    turns = db.retrieve_turns(user)
    if guesses == None:
        turns = 6
        guesses = "Please guess a letter"
    # else:
    #     turns = db.retrieve_turns(user)
    for guess_letter in guesses:
        if guess_letter in word:
            for index, letter in enumerate(word):
                if guess_letter == word[index] and guess_letter == letter:
                    guess_word[index] = letter
    return jsonify(guesses = guesses, turns = turns, word = " ".join(guess_word))

@games.route('/madlibs')
def madlibs():
    return render_template("madlibs.html")

@games.route('/rps')
def rps():
    return render_template("rockpaperscissors.html")