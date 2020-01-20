import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

print(os.environ.get("MONGO_URI"))

mongo = PyMongo(APP)

@APP.route("/")
@APP.route("/films")
def films():
    """
    Redirects to existing base template
    """
    return render_template("base.html", tasks=mongo.db.tasks.find())

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
