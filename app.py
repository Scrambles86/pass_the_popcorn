import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = 'popcorn'
APP.config["MONGO_URI"] = 'mongodb+srv://root:Kingwood1986@myfirstcluster-glpgl.mongodb.net/popcorn?retryWrites=true&w=majority'


mongo = PyMongo(APP)

@APP.route("/")
@APP.route("/films")
def films():
    """
    Redirects to existing base template
    """
    return render_template("base.html", movie_data=mongo.db.tasks.find())

if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
