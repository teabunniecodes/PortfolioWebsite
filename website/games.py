from typing import Literal
from unicodedata import category
from flask import Blueprint, render_template, request, jsonify, flash
import random

games = Blueprint('games', __name__)

@games.route("/hangman", methods=["GET", "POST"])
def hangman():
    # GET method
    if request.method == "GET":
        with open("./text documents/hangman-wordlist.txt") as read:
            words = list(map(str, read))
            chosen_word = random.choice(words)
            chosen_word = chosen_word.upper()
            guess_word = len(chosen_word) * "_ "
            print(chosen_word)
        return render_template("hangman.html", word = guess_word)
    # POST method
    if request.method == "POST":
        guess_letter = request.get_data(as_text=Literal[True])
        print(guess_letter)
        for x in range(8):
            print(guess_letter + str(x))
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