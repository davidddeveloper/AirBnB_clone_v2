#!/usr/bin/python3
"""
    a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def hbnb_states():
    """ serves a lists of states """
    from models.state import State

    states = storage.all(State)
    return render_template("9-states.html", states=states)

@app.route("/states/<string:id>", strict_slashes=False)
def hbnb_cities_by_state(id):
    """ serves a lists of states """
    from models.state import State
    from models.city import City

    states = storage.all(State)
    state = states.get("State.{}".format(id))
    cities = storage.all(City)
    return render_template("9-states.html", state=state, cities=cities)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
