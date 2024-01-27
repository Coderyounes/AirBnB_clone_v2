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
def HBNB():
    """
        Flask Function retunrn HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_fun(text):
    """
        function  use Flask Variables
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
