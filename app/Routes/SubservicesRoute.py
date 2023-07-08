from flask import Blueprint
from app.Controllers.SubservicesController import SubservicesController

SubservicesRoute = Blueprint('SubservicesRoute', __name__)

@SubservicesRoute.route('/Subservices', methods = ['GET', 'POST'])
def index():
    return SubservicesController.List()

@SubservicesRoute.route('/AddSubservice', methods = ['POST'])
def create():
    return SubservicesController.Create()

@SubservicesRoute.route('/EditSubservice/<id>/', methods = ['GET','POST'])
def edit(id):
    return SubservicesController.Edit(id)

@SubservicesRoute.route('/DeleteSubservice/<id>/', methods = ['GET','POST'])
def delete(id):
    return SubservicesController.delete(id)