from flask import Blueprint, render_template
import random

games = Blueprint('games', __name__)

@games.route("/hangman")
def hangman():
    # with open("text documents\hangman-wordlist.txt") as read:
    #     words = list(map(str, read))
    #     chosen_word = random.choice(words).strip
    #     chosen_word = chosen_word.upper()
    #     guess_word = len(chosen_word)
    return render_template("hangman.html")

@games.route('/madlibs')
def madlibs():
    return render_template("madlibs.html")

@games.route('/rps')
def rps():
    return render_template("rockpaperscissors.html")