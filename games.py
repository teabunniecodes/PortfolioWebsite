from flask import Blueprint, render_template, jsonify
import random

games = Blueprint(__name__, "games")

@games.route("/hangman")
def get_word(self):
    with open("text documents\hangman-wordlist.txt") as read:
        words = list(map(str, read))
        # self.chosen_word = random.choice(words).strip
        # self.chosen_word = self.chosen_word.upper()
        # self.guess_word = len(self.chosen_word)
    return render_template("hangman.html")
    # return jsonify(words)