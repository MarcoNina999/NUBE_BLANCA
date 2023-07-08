from flask import render_template, request,flash, redirect, url_for
from app.Forms import Forms
from app import db

from app.Models.SubservicesModel import Subservices
from app.Models.ServicesModel import Services, ServiceSubservice

class SubservicesController():
    def __init__(self):
        pass

    def List(self):
        services_form = Forms.ServicesForm(request.form)

        subservices = db.session.query(Subservices).all()
        services = db.session.query(Services).all()

        return render_template('Subservices/Subservices.html', form = services_form, subservices = subservices, services = services)

    def Create(self):
        subservice_form = Forms.ServicesForm(request.form)

        if request.method == 'POST':
            service = db.session.query(Subservices).filter(Subservices.Name == subservice_form.name.data).first()
            if service is not None:
                flash('EL SERVICIO YA EXISTE')
                return redirect(url_for('SubservicesRoute.index'))
            else:
                if db.session.query(Services).first() is None:
                    subservice = Subservices(subservice_form.name.data, subservice_form.description.data, subservice_form.price.data)

                    db.session.add(subservice)
                    db.session.commit()
                else:
                    services = request.form.getlist('services')
                    #services = ''.join(map(str, service))
                    subservice = Subservices(subservice_form.name.data, subservice_form.description.data, subservice_form.price.data)
                    db.session.add(subservice)
                    for service in services:
                        service = db.session.query(Services).filter(Services.Id == service).first()
                        subservice.ServiceSubservice.append(service)
                    db.session.commit()
                flash('SUBSERVICIO AÑADIDO EXITOSAMENTE', 'success')
                return redirect(url_for('SubservicesRoute.index'))
        else:
            return redirect(url_for('SubservicesRoute.index'))

    def Edit(self, _id):
        subservice_form = Forms.ServicesForm(request.form)

        if request.method == 'POST':
            subservice = db.session.query(Subservices).get(_id)
            serviceSubs = db.session.query(ServiceSubservice).filter(ServiceSubservice.columns[1] == _id)

            for serviceSub in serviceSubs:
                serviceSub = db.session.query(Services).filter(Services.Id == serviceSub[0]).first()
                print(serviceSub)
                subservice.ServiceSubservice.remove(serviceSub)
            
            services = request.form.getlist('services')
            for service in services:
                service = db.session.query(Services).filter(Services.Id == service).first()
                subservice.ServiceSubservice.append(service)
            
            subservice.Name = subservice_form.name.data
            subservice.Description = subservice_form.description.data
            subservice.Price = subservice_form.price.data

            db.session.commit()
            flash('SUBSERVICIO EDITADO EXITOSAMENTE', 'success')
            return redirect(url_for('SubservicesRoute.index'))
        else:
            return redirect(url_for('SubservicesRoute.index'))
    def delete(self, _id):
        subservice = Subservices.query.get(_id)
        if db.session.query(Services).first() is None:
            db.session.delete(subservice)
            db.session.commit()
            flash('SUBSERVICIO ELIMINADO EXITOSAMENTE', 'success')
            return redirect(url_for('SubservicesRoute.index'))
        else:
            serviceSubs = db.session.query(ServiceSubservice).filter(ServiceSubservice.columns[1] == _id)
            for serviceSub in serviceSubs:
                serviceSub = serviceSub[0]
            service = Services.query.get(serviceSub)

            db.session.delete(subservice)
            subservice.ServiceSubservice.remove(service)
            db.session.commit()
            flash('SUBSERVICIO ELIMINADO EXITOSAMENTE', 'success')

            return redirect(url_for('SubservicesRoute.index'))

SubservicesController = SubservicesController()