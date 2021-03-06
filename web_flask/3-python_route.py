#!/usr/bin/python3
"""
FLASK HELLO WORLD BASIC APP
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
ip = '0.0.0.0'


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_fun(text):
    r = text.replace('_', ' ')
    return "C {}".format(r)


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    r = text.replace('_', ' ')
    return "Python {}".format(r)

if __name__ == "__main__":
    """HELLO WORLD APP"""
    app.run(host=ip, port=port)
