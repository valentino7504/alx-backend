#!/usr/bin/env python3
"""

Default flask route

"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    '''default index route'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
