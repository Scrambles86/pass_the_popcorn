import os  
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
def generate_password_hash("P1ain-text-user-passw@rd", "sha256")


APP = Flask(__name__)

APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')


MONGO = PyMongo(APP)

@APP.route('/')
def index():
    return render_template('pages/index.html')

@APP.route('/login_page')
def login_page():
    return render_template('pages/loginpage.html')

@APP.route('/')
def user_login():
    if 'username' in session:
        return 'You are logged in as' + session['username']
    
    return render_template('pages/loginpage.html')

@APP.route('/login')
def login():
    return ''

@APP.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST' :
        users = MONGO.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = generate_password_hash(request.form['password'])

    return ''



@APP.route("/")
def film():
    """
    Redirects to existing base template
    """
    return render_template("pages/index.html", films=MONGO.db.movie_data.find(), title='Pass The Popcorn')

@APP.route('/core_modal')
def core_modal():
    return render_template("components/coremodal.html")

@APP.route("/reviews")
def review():
    """
    Renders review page
    """
    return render_template("pages/review.html")

@APP.route("/add_review", methods=["GET, POST"])
def add_review(posts):
    films = MONGO.db.popcorn
    films.add_review(request.form.to_dict())
    films.insert_one(posts)
    return redirect(url_for("pages/archive.html"))


@APP.route("/archive")
def archives():
    """
    Renders template for archive page
    """
    return render_template("pages/archive.html")



if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
