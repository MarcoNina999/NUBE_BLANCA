from flask import Blueprint
from app.Controllers.ServicesController import ServicesController

ServicesRoute = Blueprint('ServicesRoute', __name__)

@ServicesRoute.route('/Services', methods = ['GET', 'POST'])
def index():
    return ServicesController.List()

@ServicesRoute.route('/AddService', methods = ['POST'])
def create():
    return ServicesController.Create()

@ServicesRoute.route('/EditService/<id>/', methods = ['GET', 'POST'])
def edit(id):
    return ServicesController.Edit(id)

@ServicesRoute.route('/DeleteService/<id>/', methods = ['GET','POST'])
def delete(id):
    return ServicesController.Delete(id)