from typing import Literal
from flask import Blueprint, render_template, request, jsonify, flash, redirect
from flask_login import login_required, current_user
import random
import SQL_db

games = Blueprint('games', __name__)

@games.route('/hangman', methods=['GET', 'POST'])
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
        if db.check_id(user):
            with open("./text documents/hangman-wordlist.txt") as read:
                words = list(map(str, read))
                chosen_word = random.choice(words).strip("\n")
                chosen_word = chosen_word.upper()
                guess_word = len(chosen_word) * "_ "
            db.insert_data(user, chosen_word)
            db.commit_db()
            return render_template("hangman.html", word = guess_word)
        # if user already exists in data base this retrieves the word and sends it to the client
        else:
            chosen_word = db.retrieve_word(user)
            guesses = db.retrieve_guesses(user)
            guess_word = (len(chosen_word)) * "_ "
            return render_template("hangman.html", word = guess_word) 

    # POST method
    if request.method == "POST":
        turns = db.retrieve_turns(user)
        user_guess = request.get_data(as_text=Literal[True]).strip('"')
        guesses = db.retrieve_guesses(user)
        chosen_word = db.retrieve_word(user)
        if guesses == "":
            if user_guess not in chosen_word and len(user_guess) == 1:
                guesses = user_guess
                turns -= 1
            else:
                guesses = user_guess
        else:
            if user_guess not in guesses and len(user_guess) == 1:
                guesses = ", ".join((guesses, user_guess))
                if user_guess not in chosen_word:
                    turns -= 1
                # else:
                #     turns = db.retrieve_turns(user)
        db.update_data(guesses, turns, user)
        db.commit_db()
            # else:
            #     print("This letter was already guessed")
        if len(user_guess) == len(chosen_word):
            # if guesses == "":
            #     print("You really want to guess the full word for your first turn??")
            if user_guess != chosen_word:
                for letter in user_guess:
                    guesses = ", ".join((guesses, letter))
                turns = 0
            else:
                for letter in user_guess:
                    guesses = ", ".join((guesses, letter))
                    # db.update_data(user_guess, turns, user)
                    # db.commit_db()
            db.update_data(guesses, turns, user)
            db.commit_db()
        # Need to tie to client side so when they enter invalid option game yells at them
        else:
            pass
        return game_state_hangman()
    db.close_db()
   
@games.route('hangman/api/gamestate')
@login_required
def game_state_hangman():
    db = SQL_db.Hangman()
    db.connect_db()
    user = current_user.get_id()
    word = db.retrieve_word(user)
    guess_word = (len(word)) * "_"
    guess_word = list(map(str, guess_word))
    guesses = db.retrieve_guesses(user)
    turns = db.retrieve_turns(user)
    win = False
    if guesses == "":
        turns = 6
        guesses = ""
    for guess_letter in guesses:
        if guess_letter in word:
            for index, letter in enumerate(word):
                if guess_letter == word[index] and guess_letter == letter:
                    guess_word[index] = letter
    if "".join(guess_word) == word and turns > 0:
        win = True
    return jsonify(guesses = guesses, turns = turns, word = " ".join(guess_word), win = win)

@games.route('hangman/api/reset_game')
@login_required
def reset_game():
    db = SQL_db.Hangman()
    db.connect_db()
    user = current_user.get_id()
    db.restart_user_game(user)
    with open("./text documents/hangman-wordlist.txt") as read:
        words = list(map(str, read))
        chosen_word = random.choice(words).strip("\n")
        chosen_word = chosen_word.upper()
        guess_word = len(chosen_word) * "_ "
    db.insert_data(current_user.get_id(), chosen_word)
    db.commit_db()
    word = db.retrieve_word(user)
    guess_word = (len(word)) * "_"
    guess_word = list(map(str, guess_word))
    guesses = db.retrieve_guesses(user)
    turns = db.retrieve_turns(user)
    win = False
    return jsonify(guesses = guesses, turns = turns, word = " ".join(guess_word), win = win)

@games.route('/wordle', methods=['GET', 'POST'])
@login_required
def wordle():
    db = SQL_db.Wordle()
    db.connect_db()
    db.create_table()
    user = current_user.get_id()
    # db.clear_table()
    with open("./text documents/wordle-words.txt") as wordle_words:
        wordle_words = wordle_words.read().strip("\n")
    with open("./text documents/wordle-dictionary.txt") as dictionary:
        dictionary = dictionary.read().strip("\n")

    if request.method == "GET":
        if db.check_id(user):
            with open("./text documents/wordle-words.txt") as read:
                wordle_words = list(map(str, read))
            chosen_word = random.choice(wordle_words).strip("\n")
            db.insert_data(user, chosen_word)
            db.commit_db()
            return render_template('wordle.html')
        else:
            db.retrieve_word(user)
            return render_template('wordle.html')

    if request.method == "POST":
        user_guess = request.get_data(as_text=Literal[True]).strip('"')
        chosen_word = db.retrieve_word(user)
        guess_letters = list(user_guess)
        chosen_letters = list(chosen_word)
        words = db.retrieve_guessed_words(user)
        if user_guess in wordle_words or user_guess in dictionary:
            if words == "":
                    db.update_data(", ".join(guess_letters), user_guess, user)
            else:
                words = db.retrieve_guessed_words(user)
                words = ", ".join((words, user_guess))
                for x in user_guess:
                    letters = db.retrieve_guessed_letters(user)
                    if x not in letters:
                        letters = ", ".join((letters, x))
                        db.update_data(letters, words, user)
            for x in range(len(user_guess)):
                if guess_letters[x] == chosen_word[x]:
                    chosen_letters[x] = "*"
            for x, letter in enumerate(user_guess):
                if letter in chosen_letters:
                    if guess_letters[x] != chosen_word[x]:
                        chosen_letters[chosen_letters.index(letter)] = "*"
        db.commit_db()
    return game_state_wordle()

@games.route('/wordle/api/gamestate')
@login_required
def game_state_wordle():
    db = SQL_db.Wordle()
    db.connect_db()
    db.create_table()
    user = current_user.get_id()
    with open("./text documents/wordle-words.txt") as wordle_words:
        wordle_words = wordle_words.read().strip("\n")
    with open("./text documents/wordle-dictionary.txt") as dictionary:
        dictionary = dictionary.read().strip("\n")
    user_guess = request.get_data(as_text=Literal[True]).strip('"')
    chosen_word = db.retrieve_word(user)
    guess_letters = list(user_guess)
    chosen_letters = list(chosen_word)
    words = db.retrieve_guessed_words(user).split(', ')
    is_word = False
    is_win = False
    if user_guess in wordle_words or user_guess in dictionary:
        is_word = True
        if user_guess == chosen_word:
            is_win = True
    else:
        is_word = False
    return jsonify(user_guess = user_guess, is_word = is_word, win = is_win, words = words)


@games.route('/madlibs')
def madlibs():
    return render_template('madlibs.html')

@games.route('/rps')
def rps():
    return render_template('rockpaperscissors.html')