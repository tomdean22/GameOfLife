from os.path import abspath, dirname, join
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dev'
basedir = abspath(dirname(__file__))
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(basedir, 'data.sqlite')
app.config['SQL_ALCHEMY_TRACK_MODIFICATIONS'] = False

# the database must be defined before the blueprints are registered
db = SQLAlchemy(app=app)

from myApp.views import about_blueprint
from myApp.arena.views import play_blueprint
app.register_blueprint(about_blueprint)
app.register_blueprint(play_blueprint)
