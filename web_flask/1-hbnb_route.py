#!/usr/bin/python3
"""Flask Code with some Basic Functions"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """
        Flask Function retunrn Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def Hello():
    """
        Flask Function retunrn HBNB
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
