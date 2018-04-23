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


@app.route('/states')
@app.route('/states/<id_name>')
def states_list(id=None):
    """ state list route """
    if id_name:
        state_objs = storage.all('State').values()
        my_state = None
        for state in state_objs:
            if id_name == state.id:
                the_state = state
        return render_template('9-states.html', my_state=my_state)
    else:
        state_objs = storage.all('State').values()
        state_dict = dict([state.name, (state, )] for state in state_objs)
        return render_template('9-states.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(exception):
    '''
    After each request you must remove the current SQLAlchemy Session
    '''
    storage.close()


if __name__ == "__main__":
    """RUN APP"""
    app.run(host=ip, port=port)
