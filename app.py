import os  
from flask import Flask, render_template, redirect, request, url_for, session, escape
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# Created instance of Flask
APP = Flask(__name__)

# MongoDB settings - URI and Database name. Settings hidden in env file
APP.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
APP.config["MONGO_URI"] = os.environ.get('MONGO_URI')

#Pymongo instance created
MONGO = PyMongo(APP)

@APP.route("/")
def home():
    """
    Redirects to existing base template
    """
    return render_template("pages/index.html")

@APP.route('/')
def index():
    users = MONGO.db.users
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"

@APP.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('pages/index.html')
    return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>
	
   '''

@APP.route('/logout')
def logout():
   # remove the username from the session if it is there
    session.pop('username', None)
    return redirect('pages/index.html')


@APP.route('/<password>')
def login_page(password):

    hashed_value = generate_password_hash(password)

    stored_password = 'pbkdf2:sha256:150000$NawC8dmS$996a3db0462a554d1e3090d4d216c80642726bb65e3eb9869341caf988e3bc5d'

    result = check_password_hash(stored_password, password)

    return render_template('pages/loginpage.html')


@APP.route("/")
def film():
    """
    Redirects to existing base template
    """
    return render_template("pages/index.html", films=MONGO.db.movie_data.find(), title='Pass The Popcorn')


@APP.route("/add_review", methods=["GET, POST"])
def add_review(posts):
    films = MONGO.db.popcorn
    films.add_review(request.form.to_dict())
    films.insert_one(posts)
    return redirect(url_for("pages/userpage.html"))


@APP.route("/userpage")
def archives():
    """
    Returns users to their personal collection page
    """
    return render_template("pages/userpage.html", films=MONGO.db.movie_data.find())



if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
