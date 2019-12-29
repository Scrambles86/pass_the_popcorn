import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

from os import path
if path.exists("env.py"):
  import env 