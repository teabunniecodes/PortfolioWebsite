from flask import Flask

def create_app():
    app = Flask (__name__)
    app.config['SECRET_KEY'] = "helloworld"

    from .views import views
    from .games import games

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(games, url_prefix='/')

    return app