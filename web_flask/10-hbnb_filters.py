#!/usr/bin/python3
"""
    a script that starts a Flask web application:
"""
from flask import Flask, render_template
from models.__init__ import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_states():
    """ serves a lists of states """
    from models.state import State
    from models.city import City
    from models.amenity import Amenity

    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)

    return render_template("10-hbnb_filters.html", states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
