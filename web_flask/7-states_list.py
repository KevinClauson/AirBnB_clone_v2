#!/usr/bin/python3
"""
Flask app that renders states
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
ip = '0.0.0.0'


@app.route('/states_list')
def states_list():
    """ state list route """
    state_objs = storage.all("State")
    return render_template('7-states_list.html', state_objs=state_objs)


@app.teardown_appcontext
def teardown_db(exception):
    '''
    After each request you must remove the current SQLAlchemy Session
    '''
    storage.close()


if __name__ == "__main__":
    """RUN APP"""
    app.run(host=ip, port=port)
