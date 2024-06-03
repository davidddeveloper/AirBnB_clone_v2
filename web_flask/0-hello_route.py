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
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
