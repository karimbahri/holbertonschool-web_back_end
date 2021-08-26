#!/usr/bin/env python3
"""app.py module
    rendering html file
    using flask

"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def render_html():
    """render html:
        function that return
        the rendering the given
        html filels
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
