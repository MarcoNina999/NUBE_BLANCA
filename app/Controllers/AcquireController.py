from flask import render_template, request, flash, redirect, url_for, session
from app.Forms import Forms
from app import db

from app.Models.ServicesModel import Services, ServiceSubservice
from app.Models.SubservicesModel import Subservices
from app.Models.UsersModel import Users
from app.Models.AcquireModel import Acquire

class AcquireController():
    def __init__(self):
        pass

    def Index(self):
        if 'Administrator' in session['role']:
            acquires = db.session.query(Acquire).all()
        
            return render_template('/Acquire/ListAcquire.html', acquires = acquires)
        else:
            return redirect(url_for('AccountRoute.login'))

    def Alta(self, _id):
        acquire = Acquire.query.get(_id)

        db.session.delete(acquire)
        db.session.commit()
        flash('FUE DADO DE ALTA EXITOSAMENTE', 'success')

        return redirect(url_for('AquireRoute.index'))

    def New(self):
        subservices_form = Forms.ServicesForm(request.form)
        if 'Client' in session['role']:
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

            UserId = session['UserId']
            acquires = db.session.query(Acquire).filter(Acquire.UsersId == UserId).all()

            return render_template('/Acquire/Acquire.html', offices = offices, homes = homes, gardening = gardening, acquires = acquires)
        else:
            return redirect(url_for('AccountRoute.login'))

    def Save(self):
        if 'Cliente' in session['role']:
            if request.method == 'POST':
                UserId = session['UserId']
                acquire = Acquire(UserId, request.form['IdService'],
                                request.form['Subservices'], request.form['TotalPay'])

                db.session.add(acquire)
                db.session.commit()
                flash('ADQUIRIO EXITOSAMENTE', 'success')
            return redirect(url_for('AcquireRoute.new'))
        else:
            return redirect(url_for('AccountRoute.login'))


AcquireController = AcquireController()