import sqlite3

class User_Info():
    def connect_db(self):
        self.conn_db = sqlite3.connect("DB/database.db")
        self.db = self.conn_db.cursor()

    def create_table(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS user_info
                        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                        Created DATETIME, Username TEXT, Email TEXT, Password TEXT)""")

    def insert_data(self, date, username, email, password):
        sql = """INSERT INTO user_info(Created, Username, Email, Password)
                    VALUES (?, ?, ?, ?)"""
        self.db.execute(sql, [date, username, email, password])

    def access_email(self, email):
        self.db.execute("SELECT email FROM user_info WHERE email = ?", [email])
        if self.db.fetchone() != None:
            return True

    def access_username(self, username):
        self.db.execute("SELECT username FROM user_info WHERE username = ?", [username])
        if self.db.fetchone() != None:
            return True

    def access_password(self, password):
        self.db.execute("SELECT password FROM user_info WHERE password = ?", [password])
        if self.db.fetchone() != None:
            return True

    def access_user(self, username, password):
        self.db.execute("SELECT * FROM user_info WHERE username = ? and password = ?", [username, password])
        user = self.db.fetchone()
        if user is None:
            print("Boo!")
        else:
            return user
    
    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

# look into setting up 1 database for all games and having game_state be a JSON object (Mongo, schemaless-database, NoSQL)

# class Leader_Board():

class Hangman():
    def connect_db(self):
        self.conn_db = sqlite3.connect("DB/database.db")
        self.db = self.conn_db.cursor()

    def create_table(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS hangman
                        (id TEXT, Word TEXT, Guessed_Letters TEXT, Guesses_Left INT)""")

    def check_id(self, username):
        self.db.execute("SELECT id FROM hangman WHERE id = ?", [username])
        if self.db.fetchone() == None:
            return True

    def insert_data(self, username, word):
        sql = """INSERT INTO hangman(id, Word, Guessed_Letters, Guesses_Left)
                VALUES (?, ?, ?, ?)"""
        self.db.execute(sql, [username, word, "", 6])

    def retrieve_word(self, username):
        word = self.db.execute("SELECT Word FROM hangman WHERE id = ?", [username])
        word = word.fetchone()
        return word[0]

    def retrieve_guesses(self, username):
        guess_list = self.db.execute("SELECT Guessed_Letters FROM hangman WHERE id = ?", [username])
        guess_list = guess_list.fetchone()
        return guess_list[0]

    def retrieve_turns(self, username):
        turns = self.db.execute("SELECT Guesses_Left FROM hangman WHERE id = ?", [username])
        turns = turns.fetchone()
        return turns[0]

    def update_data(self, letters, turns, username):
        self.db.execute("UPDATE hangman SET Guessed_Letters = ?, Guesses_Left= ? WHERE id = ?", [letters, turns, username])

    def restart_user_game(self, username):
        self.db.execute("DELETE FROM hangman WHERE id = ?", [username])

    def commit_db(self):
        self.conn_db.commit()

    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

    def clear_table(self):
        self.db.execute("DROP TABLE hangman")

class Wordle():
    def connect_db(self):
        self.conn_db = sqlite3.connect("DB/database.db")
        self.db = self.conn_db.cursor()

    def create_table(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS wordle
        (id TEXT, Word TEXT, Guessed_Letters TEXT, Green_Letters TEXT, Yellow_Letters TEXT, Guessed_Words TEXT)""")

    def check_id(self, username):
        self.db.execute("SELECT id FROM wordle WHERE id = ?", [username])
        if self.db.fetchone() == None:
            return True

    def insert_data(self, username, word):
        sql = """INSERT INTO wordle(id, Word, Guessed_Letters, Green_Letters, Yellow_Letters, Guessed_Words)
                VALUES (?, ?, ?, ?, ?, ?)"""
        self.db.execute(sql, [username, word, "", "", "", ""])

    def retrieve_word(self, username):
        word = self.db.execute("SELECT Word FROM wordle where id = ?", [username])
        word = word.fetchone()
        return word[0]

    def retrieve_guessed_letters(self, username):
        letters = self.db.execute("SELECT Guessed_Letters FROM wordle where id = ?", [username])
        letters = letters.fetchone()
        return letters[0]

    def retrieve_guessed_words(self, username):
        guessed_words = self.db.execute("SELECT Guessed_Words from wordle WHERE id = ?", [username])
        guessed_words = guessed_words.fetchone()
        return guessed_words[0]

    def update_data(self, letters, guesses, username):
        self.db.execute("UPDATE wordle SET Guessed_Letters = ?, Guessed_Words = ? WHERE id = ?", [letters, guesses, username])

    def update_green_letters(self, letters, username):
        self.db.execute("UPDATE wordle SET Green_Letters = ? WHERE id = ?", [letters, username])
    
    def update_yellow_letters(self, letters, username):
        self.db.execute("UPDATE wordle SET Yellow_Letters = ? WHERE id = ?", [letters, username])

    def restart_user_game(self, username):
        self.db.execute("DELETE FROM wordle WHERE id = ?", [username])

    def commit_db(self):
        self.conn_db.commit()

    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

    def clear_table(self):
        self.db.execute("DROP TABLE wordle")

# class Mood_Tracker():
