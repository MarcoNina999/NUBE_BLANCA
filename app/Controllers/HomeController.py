from flask import render_template
from app import db

from app.Models.ServicesModel import Services, ServiceSubservice
from app.Models.SubservicesModel import Subservices

class HomeController():
    def __init__(self):
        pass
    def Index(self):

        services = db.session.query(Services.Id).all()

        serviceId = services[0][0]
        serviceSubs = db.session.query(ServiceSubservice.columns[1]).filter(ServiceSubservice.columns[0] == serviceId)
        for servicesub in serviceSubs:
            servicesub = servicesub[0]
        serviceSubs = serviceSubs[0][0]
        offices = db.session.query(Subservices).filter(Subservices.Id >= serviceSubs).filter(Subservices.Id <= servicesub).all()
        
        serviceId = services[1][0]
        serviceSubs = db.session.query(ServiceSubservice.columns[1]).filter(ServiceSubservice.columns[0] == serviceId)
        for servicesub in serviceSubs:
            servicesub = servicesub[0]
        serviceSubs = serviceSubs[0][0]
        homes = db.session.query(Subservices).filter(Subservices.Id >= serviceSubs).filter(Subservices.Id <= servicesub)

        serviceId = services[2][0]
        serviceSubs = db.session.query(ServiceSubservice.columns[1]).filter(ServiceSubservice.columns[0] == serviceId)
        for servicesub in serviceSubs:
            servicesub = servicesub[0]
        serviceSubs = serviceSubs[0][0]
        gardening = db.session.query(Subservices).filter(Subservices.Id >= serviceSubs).filter(Subservices.Id <= servicesub)

        return render_template('/Home/Index.html', offices = offices, homes = homes, gardening = gardening)
    
HomeController = HomeController()