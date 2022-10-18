from flask_login import UserMixin
import SQL_db



class User(UserMixin):
     def __init__(self, id):
          self.id = id


     @classmethod
     def find_user(cls, username, password):
          db = SQL_db.User_Info()
          db.connect_db()
          user = db.access_user(username, password)
          # returns True if the username, password exist None if user does not
          #user[2] = the username
          return cls(id = user[2])

     @classmethod
     def retrieve_id(cls, id):
          return cls(id)
          # pass

     def is_active(self):
          return self.is_active()

     def is_anonymous(self):
          return False

     def is_authenticated(self):
          return self.authenticated

     def get_id(self):
          return self.id