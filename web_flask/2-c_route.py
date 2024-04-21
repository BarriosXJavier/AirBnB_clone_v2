#!/usr/bin/python3
""" Starts a Flash Web Application C is FUN"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints when /hbnb is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints when /c is called """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    """ Main function """
    app.run(host='0.0.0.0', port=5000)
