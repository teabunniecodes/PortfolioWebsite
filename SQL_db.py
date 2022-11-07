from select import select
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

# just create new tables for each of the subsequent datas

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

    def update_data(self, list, turns, username):
        self.db.execute("UPDATE hangman SET Guessed_Letters = ?, Guesses_Left= ? WHERE id = ?", [list, turns, username])

    def restart_user_game(self, username):
        self.db.execute("DELETE FROM hangman WHERE id = ?", [username])

    def commit_db(self):
        self.conn_db.commit()

    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

    def clear_table(self):
        self.db.execute("DROP TABLE hangman")

# class Wordle():

# class Mood_Tracker():
