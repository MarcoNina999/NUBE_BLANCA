from flask import Blueprint
from app.Controllers.UsersController import UsersController
from flask_login import login_required

UsersRoute = Blueprint('UsersRoute', __name__)

@UsersRoute.route('/Users', methods = ['GET', 'POST'])
def index():
    return UsersController.List()

@UsersRoute.route('/Create', methods=['POST'])
def create():
    return UsersController.Create()

@login_required
@UsersRoute.route('/Edit/<id>/', methods=['GET', 'POST'])
def edit(id):
    return UsersController.Edit(id)

@login_required
@UsersRoute.route('/Delete/<id>/',  methods=['GET', 'POST'])
def delete(id):
    return UsersController.Delete(id)