#!/usr/bin/env python3
"""
7-app Module
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
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """Selects the language to use for localization"""
    # Get the locale from the URL parameters
    url_locale = request.args.get('locale')
    if url_locale and url_locale in Config.LANGUAGES:
        return url_locale

    # Get the locale from the user settings
    if g.user and g.user['locale'] in Config.LANGUAGES:
        return g.user['locale']

    # Get the locale from the request header
    request_locale = request.headers.get('Accept-Language')
    if request_locale:
        for language in request_locale.split(','):
            if language.split(';')[0] in Config.LANGUAGES:
                return language.split(';')[0]

    # Resort to the default locale
    return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone():
    """Selects the time zone to use for localization"""
    # Get the timezone from the URL parameters
    url_timezone = request.args.get('timezone')
    if url_timezone:
        try:
            # Validate the timezone
            return pytz.timezone(url_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Get the timezone from the user settings
    if g.user and g.user['timezone']:
        try:
            # Validate the timezone
            return pytz.timezone(g.user['timezone'])
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Resort to the default timezone
    return pytz.timezone(Config.BABEL_DEFAULT_TIMEZONE)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")
