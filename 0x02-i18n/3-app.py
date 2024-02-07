#!/usr/bin/env python3
"""
3-app Module
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """Returns index page"""
    return render_template('3-index.html',
                           title=_('home_title'),
                           header=_('home_header'))


@babel.localeselector
def get_locale():
    """Selects the language to use for localization"""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
