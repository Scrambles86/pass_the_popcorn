import os
from flask import Flask

from os import path
if path.exists("env.py"):
  import env 