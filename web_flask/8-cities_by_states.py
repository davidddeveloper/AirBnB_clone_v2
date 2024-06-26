#!/usr/bin/python3
"""
    a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def hbnb_states():
    """ serves a lists of states """
    from models.state import State
    from models.city import City

    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states, cities=cities)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
