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

@APP.route('/')
@APP.route('/index')
def index():
    return render_template("pages/index.html")

@APP.route('/personal')
def personal():
    return render_template("pages/userpage.html")

@APP.route('/formpage')
def formpage():
    return render_template("pages/loginpage.html")

@APP.route('/newsignup')
def newsignup():
    return render_template("pages/register.html")


# Login
@APP.route('/login', methods=['GET'])
def login():
    # Check if user is not logged in already
    if 'user' in session:
        user_in_db = USERS_COLLECTION.find_one({"username": session['user']})
        if user_in_db:
            # If so redirect user to his profile
            flash("You are logged in already!")
            return redirect(url_for('personal', user=user_in_db['username']))
    else:
        # Render the page for user to be able to log in
        return render_template("pages/loginpage.html")

# Check user login details from login form
@APP.route('/user_auth', methods=['POST'])
def user_auth():
    form = request.form.to_dict()
    user_in_db = USERS_COLLECTION.find_one({"username": form['username']})
    # Check for user in database
    if user_in_db:
        # If passwords match (hashed / real password)
        if check_password_hash(user_in_db['password'], form['user_password']):
            # Log user in (add to session)
            session['user'] = form['username']
            # If the user is admin redirect him to admin area
            if session['user'] == "admin":
                return redirect(url_for('admin'))
            else:
                flash("You were logged in!")
                return redirect(url_for('personal', user=user_in_db['username']))
            
        else:
            flash("Wrong password or user name!")
            return redirect(url_for('formpage'))
    else:
        flash("You must be registered!")
        return redirect(url_for('formpage'))

# Sign up
@APP.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is not logged in already
    if 'user' in session:
        flash('You are already logged in')
        return redirect(url_for('personal', user=user_in_db['username']))
    if request.method == 'POST':
        form = request.form.to_dict()
        # Check if the password and password1 actualy match 
        if form['user_password'] == form['user_password1']:
            # If so try to find the user in db
            user = USERS_COLLECTION.find_one({"username" : form['username']})
            if user:
                flash(f"{form['username']} already exists!")
                return redirect(url_for('formpage'))
            # If user does not exist register new user
            else:                
                # Hash password
                hash_pass = generate_password_hash(form['user_password'])
                #Create new user with hashed password
                USERS_COLLECTION.insert_one(
                    {
                        'username': form['username'],
                        'email': form['email'],
                        'password': hash_pass
                    }
                )
                # Check if user is actualy saved
                user_in_db = USERS_COLLECTION.find_one({"username": form['username']})
                if user_in_db:
                    # Log user in (add to session)
                    session['user'] = user_in_db['username']
                    return redirect(url_for('personal', user=user_in_db['username']))
                else:
                    flash("There was a problem savaing your profile")
                    return redirect(url_for('formpage'))

        else:
            flash("Passwords dont match!")
            return redirect(url_for('formpage'))
        
    return render_template("pages/loginpage.html")

# Log out
@APP.route('/logout')
def logout():
    # Clear the session
    session.clear()
    flash('You were logged out!')
    return redirect(url_for('index'))

# Profile Page
@APP.route('/userpage/<user>')
def profile(user): 
    # Check if user is logged in
    if 'user' in session:
        # If so get the user and pass him to template for now
        user_in_db = USERS_COLLECTION.find_one({"username": user})
        return render_template('pages/userpage.html', user=user_in_db)
    else:
        flash("You must be logged in!")
        return redirect(url_for('index'))

# @APP.route("/")
# def home():
#     """
#     Redirects to existing base template
#     """
#     return render_template("pages/index.html")

# @APP.route('/')
# def index():
#     users = MONGO.db.users
#     if 'username' in session:
#         username = session['username']
#         return 'Logged in as ' + username + '<br>' + \
#          "<b><a href = '/logout'>click here to log out</a></b>"

# @APP.route('/login', methods = ['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect('pages/index.html')
#     return '''
	
#    <form action = "" method = "post">
#       <p><input type = text name = username/></p>
#       <p<<input type = submit value = Login/></p>
#    </form>
	
#    '''

# @APP.route('/logout')
# def logout():
#    # remove the username from the session if it is there
#     session.pop('username', None)
#     return redirect('pages/index.html')


# @APP.route('/<password>')
# def login_page(password):

#     hashed_value = generate_password_hash(password)

#     stored_password = 'pbkdf2:sha256:150000$NawC8dmS$996a3db0462a554d1e3090d4d216c80642726bb65e3eb9869341caf988e3bc5d'

#     result = check_password_hash(stored_password, password)

#     return render_template('pages/loginpage.html')


# @APP.route("/")
# def film():
#     """
#     Redirects to existing base template
#     """
#     return render_template("pages/index.html", films=MONGO.db.movie_data.find(), title='Pass The Popcorn')


# @APP.route("/add_review", methods=["GET, POST"])
# def add_review(posts):
#     films = MONGO.db.popcorn
#     films.add_review(request.form.to_dict())
#     films.insert_one(films)
#     return redirect(url_for("pages/userpage.html"))


# @APP.route("/userpage")
# def archives():
#     """
#     Returns users to their personal collection page
#     """
#     return render_template("pages/userpage.html", films=MONGO.db.movie_data.find())



if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
