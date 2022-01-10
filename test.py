import os
import sys


sys.path.append('/home/c/cx56944/myenv/lib/python3.6/site-packages/')
from flask import Flask, render_template

app = Flask(__name__)
application = app


@app.route('/')
def hello_world():
    return 'wen'


if __name__ == '__main__':
    app.run(debug=True)
