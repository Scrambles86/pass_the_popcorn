import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

print(os.environ.get("MONGO_URI"))

mongo = PyMongo(APP)

@APP.route("/")
def hello():
    """
    This is the test function
    """
    return "Hello, Flask!"

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
