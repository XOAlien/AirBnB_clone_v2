#!/usr/bin/python3
'''starts a Flask web application'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''prints Hello HBNB'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''print HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    '''prints C followed by input text'''
    c_text = 'C {}'.format(text)
    c_text = c_text.replace('_', ' ')
    return c_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
