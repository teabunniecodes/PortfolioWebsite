from flask import Blueprint, render_template, request, flash
from hashlib import sha256
import SQL_db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/user', methods=['GET', 'POST'])
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
        password1 = sha256((request.form.get("password1")).encode()).hexdigest()
        password2 = sha256((request.form.get("password2")).encode()).hexdigest()

        # username_exists = ???.filter_by(username = username).first()
        # email_exists = ???.filter_by(email = email).first()
        # if email_exists:
        #     flash('Email is already in use', category = 'error')
        # elif username_exists:
        #     flash('Username is already in use', category = 'error')
        if len(password1) < 6:
            flash('Password is too short!', category = 'error')
            print('Password is too short!')
        elif password1 != password2:
            flash('Password doesn\'t match!', category = 'error')
            print('Password doesn\'t match!')
        else:
            database = SQL_db.User_Info()
            database.connect_db()
            database.create_table()
            database.insert_data(created, username, email, password1)
            database.close_db()
            print('User Created')
    return render_template("signup.html")