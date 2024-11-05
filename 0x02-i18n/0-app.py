#!/usr/bin/env python3
"""

Default flask route

"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    '''default index route'''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
