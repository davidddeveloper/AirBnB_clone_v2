#!/usr/bin/python3
"""
    a script that starts a Flask web application:
"""
from flask import Flask
from models.__init__ import storage

app = Flask(__name__, strict_slashes=False)


@app.route("/states_list")
def hbnb_states():
    """ serves a lists of states """
    from models.state import State

    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
