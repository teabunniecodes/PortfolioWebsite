import sqlite3

class User_Info:
    def connect_db(self):
        self.conn_db = sqlite3.connect("DB/user_info.db")
        # learn more about cursors for SQL and python
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
    
    def close_db(self):
        self.conn_db.commit()
        self.conn_db.close()

# class Hangman:
#     self.conn_db = sqlite3.connect("hangman.db")