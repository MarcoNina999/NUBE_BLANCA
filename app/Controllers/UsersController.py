from flask import render_template, request, flash, redirect, url_for, session
from app.Forms import Forms
from app import db

from app.Models.UsersModel import Users, UserRole
from app.Models.RolesModel import Roles

class UsersController():
    def __init__(self):
        pass
    
    def List(self):
        if 'username' in session:
            users_form = Forms.UsersForm(request.form)
        
            users = Users.query.all()
            roles = Roles.query.all()

            return render_template('Users/Users.html', form = users_form, users = users, roles = roles)
        else:
            return redirect(url_for('AccountRoute.login'))
    
    def Create(self):
        users_form = Forms.UsersForm(request.form)

        if request.method == 'POST':
            user = Users.query.filter(Users.Email == request.form['email']).first()
            if user is not None:
                flash('EL USUARIO QUE INGRESO YA EXISTE', 'warning')
                return redirect(url_for('UsersRoute.index'))
            else:
                role = request.form['role']
                role = Roles.query.filter_by(Id = role).first()
                user = Users(request.form['name'], request.form['ci'], request.form['address'],
                                request.form['phone'], request.form['email'], request.form['ci'])
                db.session.add(user)
                role.UserRole.append(user)
                # db.session.add(role)
                db.session.commit()
                flash('REGISTRO EXITOSO', 'success')
                return redirect(url_for('UsersRoute.index'))
        else:
            return redirect(url_for('UsersRoute.index'))
        
    def Edit(Self, _id):
        users_form = Forms.UsersForm()

        if request.method == 'POST':
            name = request.form['name']
            ci = request.form['ci']
            address = request.form['address']
            phone = request.form['phone']
            email = request.form['email']

            user = Users.query.get(_id)
            user.Name = name
            user.CI = ci
            user.Address = address
            user.Phone = phone
            user.Email = email

            db.session.commit()
            flash('SE EDITO EXITOSO', 'success')
            return redirect(url_for('UsersRoute.index'))
        else:
            return redirect(url_for('UsersRoute.index'))

    def Delete(self, _id):
        user = Users.query.get(_id)
        user_roles = db.session.query(UserRole).filter(UserRole.columns[0] == _id)
        for user_role in user_roles:
            user_role = user_role[1]
        role = Roles.query.get(user_role)

        db.session.delete(user)
        role.UserRole.remove(user)
        db.session.commit()
        flash('ELIMINACIÓN EXITOSA', 'success')

        return redirect(url_for('UsersRoute.index'))

UsersController = UsersController() 