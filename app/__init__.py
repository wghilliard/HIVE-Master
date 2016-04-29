from flask import Flask
from flask.ext.admin.base import Admin
# from flask.ext.api import FlaskAPI
from flask.ext.mongoengine import MongoEngine


# import config

# Flask
app = Flask(__name__)
app.config.from_object('config')

# MongoDB
db = MongoEngine(app)

# Flask-Admin
admin = Admin(app, name='Lariatsoft', template_mode='bootstrap3')

import views, api




