from flask import Blueprint
from app.Controllers.AcquireController import AcquireController

AcquireRoute = Blueprint('AcquireRoute', __name__)

@AcquireRoute.route('/ListAcquire', methods = ['GET','POST'])
def list():
    return AcquireController.Index()

@AcquireRoute.route('/Alta/<id>/', methods = ['GET','POST'])
def alta(id):
    return AcquireController.Alta(id)

@AcquireRoute.route('/Acquire', methods = ['GET','POST'])
def new():
    return AcquireController.New()


@AcquireRoute.route('/SaveAcquire', methods=['GET', 'POST'])
def save():
    return AcquireController.Save()