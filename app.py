import os  
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')


MONGO = PyMongo(APP)

@APP.route('/')
def index():
    if 'username' in session: 
        return 'You are logged in as ' + session['username']
    
    return render_template('pages/index.html')

@APP.route('/login' method=["POST"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'Invalid username/password combination'
    

@APP.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.haspw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' = hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists'
    return render_template('register.html')
    return ''

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


@APP.route("/reviews/<review_id>")
def review_ind(review_id):
    return render_template("pages/review/<review_id>.html")


@APP.route("/add_review", methods=["POST"])
def add_review():
    films = MONGO.db.films
    films.add_review(request.form.to_dict())
    posts.insert_one()
    return redirect (url_for("pages/review.html"))


@APP.route("/reviews/edit/<review_id>")
def edit_review(review_id):
    return render_template("pages/review.html")


@APP.route("/reviews/delete/<review_id>")
def delete_review(review_id):
    return render_template("pages/review.html")


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


@APP.route("/api/movie/add", methods=["POST"])
def add_movie(newMovie):
    return newMovie


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)