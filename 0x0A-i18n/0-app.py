#!/usr/bin/env python3
"""app"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def render_html():
    """render html:
        function that return the rendering html file
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
