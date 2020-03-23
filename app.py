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
    """
    Renders review page
    """
    return render_template("pages/review.html")

@APP.route("/reviews/<review_id>")
def add_review(review_id):
    return render_template("pages/review.html")
   

@APP.route("/reviews/add")
def add_review(review_id):
    return render_template("pages/review.html")
    

@APP.route("/reviews/edit/<review_id>")
def add_review(review_id):
    return render_template("pages/review.html")
    

@APP.route("/reviews/delete/<review_id>")
def add_review(review_id):
    return render_template("pages/review.html")
    

@APP.route("/archive")
def archives():
    return render_template("pages/archive.html")
    

@APP.route("/mypage")
def userpage():
    return render_template("pages/mypage.html")
    

@APP.route("/index")
def homepage():
    return render_template("pages/index.html")
    


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
