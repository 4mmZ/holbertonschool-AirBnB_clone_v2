#!/usr/bin/python3
""" document """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """ document """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ display hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """ display C """
    text_with_spaces = text.replace("_", " ")
    return f"C {text_with_spaces}"


@app.route('/python/<text>', strict_slashes=False)
def display_Python(text= "is cool"):
    """ display Python"""
    text_w_spaces = text.replace("_", " ")
    return f"Python {text_w_spaces}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
