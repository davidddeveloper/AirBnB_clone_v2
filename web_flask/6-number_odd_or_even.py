#!/usr/bin/python3
"""
    a script that starts a Flask web application:
        listening on 0.0.0.0
        port 5000

    contain the following function
    hello
"""

from flask import Flask, render_template


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


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>")
def hbnb_python(text="is cool"):
    """ takes a value and returns it """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>")
def hbnb_number(n):
    """ takes a number and returns it
        only if it is an integer """

    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def hbnb_number_template(n):
    """ takes a number and returns it in a template
        only if it is an integer """

    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def hbnb_number_template_odd_or_even(n):
    """ takes a number and returns it in a template
        only if it is an integer """

    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
