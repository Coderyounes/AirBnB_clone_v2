#!/usr/bin/python3
"""Flask Code with some Basic Functions"""
from flask import Flask
from flask import render_template

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
    """
        display the n if it int
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def templ(n):
    """
        Flask Function use template rendring & Jinja
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n):
    """
        Function Check if the number is even or odd
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
