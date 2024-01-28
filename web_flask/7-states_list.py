#!/usr/bin/python3
""" Flask app list all State & Close after finish"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_state():
    """
        Flask Function list all the state
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def termination():
    """ Close the ORM Sessions after finish"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
