import os  
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# Created instance of Flask
APP = Flask(__name__)

# MongoDB settings - URI and Database name. Settings hidden in env file
APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')
APP.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

#Pymongo instance created
MONGO = PyMongo(APP)

# Collections

USERS_COLLECTION = MONGO.db.users
MOVIE_COLLECTION = MONGO.db.movie_data

# Page Rendering

@APP.route('/')
@APP.route('/index')
def index():
    """

    Renders Index Page

    """
    return render_template("pages/index.html")

@APP.route('/personal')
def personal():
    """

    Renders User Page

    """
    return render_template("pages/userpage.html")

@APP.route('/formpage')
def formpage():
    """

    Renders login Page

    """
    return render_template("pages/loginpage.html")

@APP.route('/newsignup')
def newsignup():
    """

    Renders register Page

    """
    return render_template("pages/register.html")


# Login
@APP.route('/login', methods=['GET'])
def login():
    """
    Checks if user is logged in and redirects to their collection page if so.
    """
    if 'user' in session:
        user_in_db = USERS_COLLECTION.find_one({"username": session['user']})
        if user_in_db:
            return redirect(url_for('personal', user=user_in_db['username']))
    else:

        return render_template("pages/loginpage.html")

# Check user login details from login form
@APP.route('/user_auth', methods=['POST'])
def user_auth():
    """
    Checks if user is in DB
    Makes sure that password matches hashed password
    Adds user to session and redirects to their collection
    Flashes error and redirects user if user doesn't exist
    """
    form = request.form.to_dict()
    user_in_db = USERS_COLLECTION.find_one({"username": form['username']})
    if user_in_db:
        if check_password_hash(user_in_db['password'], form['password']):
            session['user'] = form['username']
            return redirect(url_for('personal', user=user_in_db['username']))           
        else:
            flash("Incorrect password or user name")
            return redirect(url_for('formpage'))
    else:
        flash("No user found. Please register")
        return redirect(url_for('formpage'))

# Sign up
@APP.route('/register', methods=['GET', 'POST'])
def register():
    """
    Ensures user is not already logged in.
    Ensures passwords both match, then checks DB to make sure that username isn't already taken
    New user generated if not
    Password hashed so that passwords aren't saved in DB
    Logs user in, adding them to session
    """
    if 'user' in session:
        flash('You are already logged in')
        return redirect(url_for('personal', user=user_in_db['username']))
    if request.method == 'POST':
        form = request.form.to_dict()
        if form['user_password'] == form['user_password1']:
            user = USERS_COLLECTION.find_one({"username" : form['username']})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for('formpage'))
            else:                
                hash_pass = generate_password_hash(form['user_password'])
                USERS_COLLECTION.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_pass
                    }
                )
                user_in_db = USERS_COLLECTION.find_one({"username": form['username']})
                if user_in_db:
                    session['user'] = user_in_db['username']
                    return redirect(url_for('personal', user=user_in_db['username']))
                else:
                    flash("Sorry, something went wrong")
                    return redirect(url_for('formpage'))
        else:
            flash("Passwords dont match!")
            return redirect(url_for('formpage'))     
    return render_template("pages/loginpage.html")

# Log out
@APP.route('/logout')
def logout():
    """
    Clears session, signing out user
    """
    session.clear()
    flash('You were logged out!')
    return redirect(url_for('index'))

# Profile Page
@APP.route('/userpage/<user>')
def profile(user): 
    """
    Checks if user is logged in and redirects to their collection page if so.
    If not, user is redirected to login page
    """
    if 'user' in session:
        user_in_db = USERS_COLLECTION.find_one({"username": user})
        return render_template('pages/userpage.html', user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('login'))


@APP.route("/add_review", methods=["POST"])
def add_review():
    if 'user' in session:
        films = MONGO.db.popcorn
        films.add_review(request.form.to_dict())
        MOVIE_COLLECTION.insert_one(
            {
                'movie-poster': request.form.get('movie-poster'),
                'movie-title': request.form.get('movie-title'),
                'movie-director': request.form.get('movie-director'),
                'movie-year': request.form.get('movie-year'),
                'movie-actor': request.form.get('movie-actor'),
                'movie-genre': request.form.get('movie-genre'),     
            }
        )
        return redirect('pages/userpage.html')
    else:
        flash("Please log in to add to your collection")
        return redirect(url_for('login'))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
