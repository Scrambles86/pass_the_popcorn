import os  
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')


MONGO = PyMongo(APP)

@APP.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    return redirect("/" + email + "/" + password + "/" + username)

@APP.route('/<email>/<username>/<password>')
def user_collection(email, password, username):
    return render_template('pages/mypage.html', username=username)

@APP.route("/")
def films():
    """
    Redirects to existing base template
    """
    return render_template("pages/index.html", films=MONGO.db.movie_data.find(), title='Pass The Popcorn', signup=False)


@APP.route("/reviews")
def review():
    """
    Renders review page
    """
    return render_template("pages/review.html")



@APP.route("/add_review", methods=["POST"])
def add_review(posts):
    films = MONGO.db.films
    films.add_review(request.form.to_dict())
    posts.insert_one()
    return redirect(url_for("pages/review.html"))


@APP.route("/archive")
def archives():
    """
    Renders template for archive page
    """
    return render_template("pages/archive.html")


@APP.route("/mypage")
def userpage():
    """
    Render template for users personal page
    """
    return render_template("pages/mypage.html")


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
