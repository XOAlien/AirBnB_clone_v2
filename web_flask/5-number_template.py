#!/usr/bin/python3
'''prints number if its integer'''
from flask import Flask
from flask import render_template
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
    '''prints number <n> if it is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    '''displays HTML page if <n> is an integer'''
    return render_template('5-number.html', num=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
