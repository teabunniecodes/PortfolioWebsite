from flask import Blueprint, render_template, request, flash
from hashlib import sha256
import SQL_db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.get('/user')
def user():
    database = SQL_db.User_Info()
    database.connect_db()
    database.create_table()
    username = request.form.get("username")
    password = sha256((request.form.get("password")).encode).hexdigest()
    username_exists = database.access_username(username)
    database.close_db()
    return render_template("user.html")

@views.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        database = SQL_db.User_Info()
        database.connect_db()
        database.create_table()
        from datetime import date
        created = date.today()
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email_exists = database.access_email(email)
        username_exists = database.access_username(username)
        if email_exists:
            flash("Email is already in use")
        elif username_exists:
            flash("Username is already in use")
        elif len(password1) < 6:
            flash("Password is too short!")
        elif password1 != password2:
            flash("Passwords don't match")
        else:
            password1 = sha256((password1).encode()).hexdigest()
            database.insert_data(created, username, email, password1)
            flash('User Created')
        database.close_db()
    return render_template("signup.html")