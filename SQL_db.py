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

    def access_email(self, inquiry):
        self.db.execute("SELECT email FROM user_info WHERE email = ?", [inquiry])
        if self.db.fetchone() != None:
            return True

    def access_username(self, inquiry):
        self.db.execute("SELECT username FROM user_info WHERE username = ?", [inquiry])
        if self.db.fetchone() != None:
            return True

    def access_password(self, inquiry):
        self.db.execute("SELECT password FROM user_info WHERE password = ?", [inquiry])
        if self.db.fetchone() != None:
            return True

    def access_user(self, inquiry1, inquiry2):
        self.db.execute("SELECT * FROM user_info WHERE username = ? and password = ?", [inquiry1, inquiry2])
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

    def insert_data(self, inquiry, inquiry2):
        sql = """INSERT INTO hangman(id, Word)
                VALUES (?, ?)"""
        self.db.execute(sql, [inquiry, inquiry2])

    # def update_guesses(self):

    def get_word(self, inquiry):
        word = self.db.execute("SELECT Word FROM hangman WHERE id = ?", [inquiry])
        word = word.fetchone()
        return word[0]

    def check_id(self, inquiry):
        self.db.execute("SELECT id FROM hangman WHERE id = ?", [inquiry])
        if self.db.fetchone() == None:
            return True

    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

    def clearTable(self):
        self.db.execute("DROP TABLE hangman")

# class Wordle():

# class Mood_Tracker():
