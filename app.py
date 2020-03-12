import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')


MONGO = PyMongo(APP)

@APP.route("/")
def films():
    """
    Redirects to existing base template
    """
    return render_template("pages/index.html", films=MONGO.db.movie_data.find(), title='Pass The Popcorn')

@APP.route("/reviews")
def add_review():
    return render_template("reviews")
    @APP.route("pages/reviews.html")

@APP.route("/reviews/<review_id>")
def add_review(review_id):
    return render_template("reviews")
    @APP.route("/add_review")

@APP.route("/reviews/add")
def add_review(review_id):
    return render_template("reviews")
    @APP.route("/add_review")

@APP.route("/reviews/edit/review_id")
def add_review(review_id):
    return render_template("reviews")
    @APP.route("/add_review")

@APP.route("/reviews/delete/review_id")
def add_review(review_id):
    return render_template("reviews")
    @APP.route("/add_review")



if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
