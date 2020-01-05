from flask import Flask
from flask_pymongo import PyMongo

import app.routes as main
import app.conf as conf

app = Flask(__name__)























conf.db(app)
main.serve(app, PyMongo)
