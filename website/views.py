from flask import Blueprint, render_template, request, flash, redirect, url_for
from hashlib import sha256
# hashlib.scrypt look into that once I start working on tighter security
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
import SQL_db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        database = SQL_db.User_Info()
        database.connect_db()
        username = request.form.get("username")
        password = sha256((request.form.get("password")).encode()).hexdigest()
        # checks if the username and password matches an account in the DB
        if User.find_user(username, password):
            login_user(User.find_user(username, password), remember = True, force = True)
            flash("Log in successful for", category = "success")
        # if not in database, will give error if the username or password is incorrect
        elif not database.access_username(username):
            flash("Invalid Username", category = "error")
        elif not database.access_password(password):
            flash("Invalid Password", category = "error")
        database.close_db()
    return render_template("user.html")

@views.route('/logout')
@login_required
def logout():
    logout_user()
    print("Logged Out")
    return redirect('/')


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
        # email_exists = database.access_email(email)
        # username_exists = database.access_username(username)
        if database.access_email(email):
            flash("Email is already in use")
        elif database.access_username(username):
            flash("Username is already in use")
        elif len(password1) < 6:
            flash("Password is too short!")
        elif password1 != password2:
            flash("Passwords don't match")
        else:
            password1 = sha256((password1).encode()).hexdigest()
            database.insert_data(created, username, email, password1)
            flash('User Created')
            login_user(User.retrieve_id(username), remember = True)
        database.close_db()
    return render_template("signup.html")