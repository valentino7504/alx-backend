#!/usr/bin/env python3
"""

Default flask route

"""
from flask import Flask, render_template
from flask_babel import Babel, request


app = Flask(__name__)


class Config():
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''determine match'''
    return request.args.get('lang', Config.BABEL_DEFAULT_LOCALE)


@app.route('/')
def index():
    '''default index route'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
