import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)