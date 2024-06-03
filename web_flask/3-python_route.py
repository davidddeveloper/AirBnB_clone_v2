#!/usr/bin/python3
"""
    a script that starts a Flask web application:
        listening on 0.0.0.0
        port 5000

    contain the following function
    hello
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb_hello():
    """ handle / route """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ handles the /hbnb route """
    return "HBNB"


@app.route("/c/<text>")
def hbnb_c(text):
    """ takes a value and returns it """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>")
def hbnb_python(text):
    """ takes a value and returns it """
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
