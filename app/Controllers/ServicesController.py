from flask import render_template, request,flash, redirect, url_for
from app.Forms import Forms
from app import db

from app.Models.ServicesModel import Services, ServiceSubservice
from app.Models.SubservicesModel import Subservices

class ServicesController():
    def __init__(self):
        pass

    def List(self):
        services_form = Forms.ServicesForm(request.form)

        services = db.session.query(Services).all()
        subservices = db.session.query(Subservices).all()

        return render_template('Services/Services.html', form = services_form, services = services, subservices = subservices)

    def Create(self):
        service_form = Forms.ServicesForm(request.form)

        if request.method == 'POST':
            service = db.session.query(Services).filter(Services.Name == service_form.name.data).first()
            if service is not None:
                flash('EL SERVICIO YA EXISTE', 'warning')
                return redirect(url_for('ServicesRoute.index'))
            else:
                if db.session.query(Subservices).first() is None:
                    service = Services(service_form.name.data, service_form.description.data)

                    db.session.add(service)
                    db.session.commit()
                else:
                    subservices = request.form.getlist('subservices')
                    service = Services(service_form.name.data, service_form.description.data)
                    db.session.add(service)
                    for subservice in subservices:
                        subservice = db.session.query(Subservices).filter(Subservices.Id == subservice).first()
                        subservice.ServiceSubservice.append(service)
                    db.session.commit()
                flash('SERVICIO AÑADIDO EXITOSAMENTE', 'success')
                return redirect(url_for('ServicesRoute.index'))
        else:
            return redirect(url_for('ServicesRoute.index'))

    def Edit(self, _id):
        service_form = Forms.ServicesForm(request.form)

        if request.method == 'POST':
            service = db.session.query(Services).get(_id)
            serviceSubs = db.session.query(ServiceSubservice).filter(ServiceSubservice.columns[0] == _id)

            for serviceSub in serviceSubs:
                subservice = db.session.query(Subservices).filter(Subservices.Id == serviceSub[1]).first()
                subservice.ServiceSubservice.remove(service)
            
            subservices = request.form.getlist('subservices')
            for subservice in subservices:
                subservice = db.session.query(Subservices).filter(Subservices.Id == subservice).first()
                subservice.ServiceSubservice.append(service)
            
            service.Name = service_form.name.data
            service.Description = service_form.description.data

            db.session.commit()
            flash('SERVICIO EDITADO EXITOSAMENTE', 'success')
            return redirect(url_for('ServicesRoute.index'))
        else:
            return redirect(url_for('ServicesRoute.index'))
        
    def Delete(self, _id):
        service = Services.query.get(_id)
        if db.session.query(Subservices).first() is None:
            db.session.delete(service)
            db.session.commit()
            flash('SERVICIO ELIMINADO EXITOSAMENTE', 'success')
            return redirect(url_for('ServicesRoute.index'))
        else:
            serviceSubs = db.session.query(ServiceSubservice).filter(ServiceSubservice.columns[0] == _id)
            for serviceSub in serviceSubs:
                serviceSub = serviceSub[1]
            subservice = Subservices.query.get(serviceSub)

            db.session.delete(service)
            subservice.ServiceSubservice.remove(service)
            db.session.commit()
            flash('SERVICIO ELIMINADO EXITOSAMENTE', 'success')

            return redirect(url_for('ServicesRoute.index'))

ServicesController = ServicesController()