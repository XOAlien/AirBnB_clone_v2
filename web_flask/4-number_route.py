#!/usr/bin/python3
'''starts Flask web app, prints number if its integer'''
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text='is cool'):
    '''prints Python followed by input text'''
    py_text = 'Python {}'.format(text)
    py_text = py_text.replace('_', ' ')
    return py_text


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    '''prints number if it is an integer'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
