from flask import Blueprint, session, request, redirect, url_for
from app.Controllers.HomeController import HomeController
from app.Controllers.AccountController import AccountController
""" import Forms """

AccountRoute = Blueprint('AccountRoute', __name__)

@AccountRoute.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['Route.index']:
        return redirect(url_for('AccountRoute.login'))
    elif 'username' in session and request.endpoint in ['Route.login', 'Route.register']:
        return redirect(url_for('AccountRoute.index'))

@AccountRoute.route('/index', methods = ['GET', 'POST'])
@AccountRoute.route('/', methods = ['GET', 'POST'])
def index():
    return HomeController.Index()

@AccountRoute.route('/Login', methods = ['GET','POST'])
def login():
    return AccountController.Login()

@AccountRoute.route('/Register', methods = ['GET', 'POST'])
def register():
    return AccountController.Register()

@AccountRoute.route('/Logout')
def logout():
    return AccountController.Logout()