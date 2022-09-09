from flask import Flask
from games import games

app = Flask(__name__)
app.register_blueprint(games, url_prefix="/hangman")

if __name__== 'main':
    app.run(debug=True)