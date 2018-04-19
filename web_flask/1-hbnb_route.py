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


if __name__ == "__main__":
    """HELLO WORLD APP"""
    app.run(host=ip, port=port)
