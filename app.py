import os  
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

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


# Login function

@APP.route('/login', methods=['GET'])
def login():
    """
    Checks if user is logged in and redirects to their collection page if so.
    """
    if 'user' in session:
        user_in_db = USERS_COLLECTION.find_one({"username": session['user']})
        if user_in_db:
            flash("Logged in as {} - Welcome!".format(request.form.get("username")))
            return redirect(url_for('personal', user=user_in_db['username']))
    else:
        return redirect(url_for('personal'))

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

# Register function for new users
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
        flash("You are already logged in")
        return redirect(url_for('personal'))
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
    return redirect(url_for('formpage'))

# Log out
@APP.route('/logout')
def logout():
    """
    Clears session, signing out user
    """
    session.clear()
    flash("Logged out successfully")
    return redirect(url_for('index'))

# User's Profile Page
@APP.route('/userpage/<user>')
def profile(user): 
    """
    Checks if user is logged in and redirects to their collection page if so.
    If not, user is redirected to login page
    """
    if 'user' in session:
        user_in_db = USERS_COLLECTION.find_one({"username": user})
        return redirect(url_for('personal', user=user_in_db))
    else:
        flash("You must be logged in!")
        return redirect(url_for('login'))

# Add film to database
@APP.route("/add_review", methods=["GET, POST"])
def add_review():
    if 'user' in session:
        user_in_db = USERS_COLLECTION.find_one({"username": session['user']})
        MOVIE_COLLECTION.insert_one(
            {
                'movie-poster': request.form.get('movie-poster'),
                'movie-title': request.form.get('movie-title'),
                'movie-director': request.form.get('movie-director'),
                'movie-year': request.form.get('movie-year'),
                'movie-actor': request.form.get('movie-actor'),
                'movie-genre': request.form.get('movie-genre'),
                'reviewed-by': session['user'],  
            }
        )
        flash("Movie logged to your collection!")
        for MOVIE_COLLECTION.find({"reviewed-by": session['user']})
        print (MOVIE_COLLECTION)
        return redirect(url_for('personal', user=user_in_db, user_collection=user_collection))
    else:
        flash("Please log in to add to your collection")
        return redirect(url_for('login'))

# Delete Film from Database
@APP.route('/delete_movie/<movie_id>', methods=['GET', 'POST'])
def delete_movie(movie_id):
    if request.method == "POST":
        film = MONGO.db.movie_data
        film.delete_one({'_id': ObjectId(movie_id)})
    return redirect(url_for('personal'))


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
