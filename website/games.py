from flask import Blueprint, render_template, request, jsonify
import random

games = Blueprint('games', __name__)

@games.route("/hangman", methods=["GET", "POST"])
def hangman():
    with open("./text documents/hangman-wordlist.txt") as read:
        words = list(map(str, read))
        chosen_word = random.choice(words)
        chosen_word = chosen_word.upper()

    # GET method
    if request.method == "GET":
        guess_word = len(chosen_word) * "_ "

    # POST method
    if request.method == "POST":
        guess_letter = request.form.get("letter")

    return render_template("hangman.html", word = guess_word)

@games.route('/madlibs')
def madlibs():
    return render_template("madlibs.html")

@games.route('/rps')
def rps():
    return render_template("rockpaperscissors.html")

# figure out how to send "word" to client side
# figure out how to pull random word from word list and send to client side
# figure out to send only length of word to client side
# figure out how to send guess from client side back to server to check