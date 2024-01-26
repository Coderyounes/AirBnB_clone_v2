#!/usr/bin/python3
""" Basic Flask Code SHow Hello HBHB"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """
        Flask Function retunrn Hello HBNB
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
