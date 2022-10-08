from flask import Blueprint, render_template, request, flash
from hashlib import sha256
import SQL_db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.get('/user')
def user():
    username = request.form.get("username")
    password = request.form.get("password")
    database = SQL_db.User_Info()
    database.connect_db()
    database.close_db()
    return render_template("user.html")

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        from datetime import date
        created = date.today()
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if password1 == password2:
            password1 = sha256((password1).encode()).hexdigest()
        else:
            print("Passwords don't match")

        # username_exists = ???.filter_by(username = username).first()
        # email_exists = ???.filter_by(email = email).first()
        # if email_exists:
        #     flash('Email is already in use', category = 'error')
        # elif username_exists:
        #     flash('Username is already in use', category = 'error')
        if len(password1) < 6:
            flash('Password is too short!', category = 'error')
            print('Password is too short!')
        else:
            database = SQL_db.User_Info()
            database.connect_db()
            database.create_table()
            database.insert_data(created, username, email, password1)
            database.close_db()
            print('User Created')
    return render_template("signup.html")