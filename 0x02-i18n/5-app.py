#!/usr/bin/env python3
"""
5-app Module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Retrieve user information based on user ID"""
    return users.get(int(user_id))


@app.before_request
def before_request():
    """Execute before all other functions"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """Returns index page"""
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """Selects the language to use for localization"""
    # Get the locale from the user if logged in
    if g.user and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']
    # Resort to the default behavior
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
