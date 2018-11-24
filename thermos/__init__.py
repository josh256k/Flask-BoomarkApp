import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment


# Application setup file

# Determine to the current python file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '_5#y2L&@$$GDH122?"F4Q8z'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/thermos.db'
db = SQLAlchemy(app)

# Configure authentiation
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

moment = Moment(app)

from thermos import models
from thermos import views




