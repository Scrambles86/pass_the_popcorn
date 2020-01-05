import os
from flask import Flask
from flask_pymongo import PyMongo


@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
