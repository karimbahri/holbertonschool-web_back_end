#!/usr/bin/env python3
"""app.py module
    rendering html file
    using flask

"""
import babel
import flask
from flask import Flask
from flask import render_template
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """
    config class
    class attributes:

        LANGUAGES
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)

app.config.from_object(Config)


@app.route('/')
def render_html():
    """render html:
        function that return
        the rendering the given
        html filels
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """get_locale:
        function to find the best match language
        return : request.accept_languages.best_match
    """
    return flask.request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
