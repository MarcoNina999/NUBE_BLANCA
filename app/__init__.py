__version__ = "0.1"
import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from decouple import config

# app = Flask(__name__)
UPLOAD_FOLDER = 'app/static/Images/'
app = Flask(__name__, template_folder = "Views")
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['SESSION_TYPE'] = 'memcached'

dbConnection = 'mysql+pymysql://' + config('MYSQL_USER') + '@' + config('MYSQL_HOST') + '/' + config('MYSQL_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = dbConnection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

app.debug = True

from app.Routes.AccountRoute import AccountRoute
app.register_blueprint(AccountRoute)
from app.Routes.UsersRoute import UsersRoute
app.register_blueprint(UsersRoute)
from app.Routes.ServicesRoute import ServicesRoute
app.register_blueprint(ServicesRoute)
from app.Routes.SubservicesRoute import SubservicesRoute
app.register_blueprint(SubservicesRoute)
from app.Routes.AcquireRoute import AcquireRoute
app.register_blueprint(AcquireRoute)