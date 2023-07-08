from flask import render_template, flash, request, redirect, url_for, session
from app.Forms import Forms
from app import db

from app.Models.UsersModel import Users, UserRole
from app.Models.RolesModel import Roles

class AccountController():
    def __init__(self):
        pass

    def Login(self):
        login_form = Forms.UsersForm(request.form)

        if request.method == 'POST':
            try:

                email = login_form.email.data
                password = login_form.password.data
                user = db.session.query(Users).filter(Users.Email == email).first()
                if user is  not None:
                    userId = db.session.query(Users.Id).filter(Users.Email == email).all()
                    userId = userId[0][0]
                    print(user)
                    user_role = db.session.query(UserRole.columns[1]).filter(UserRole.columns[0] == userId).all()
                    user_role = user_role[0][0]
                    print(user_role)
                    role = db.session.query(Roles.Name).filter(Roles.Id == user_role).first()
                    role = role[0]

                    # Account doesnt exist or username/password incorrect
                    if user.__verify_passwrod__(password):
                        name = user.Name
                        flash('INICIO DE SESION EXITOSA', 'success')
                        session['UserId'] = userId
                        session['username'] = name
                        session['email'] = email
                        session['role'] = role
                        return redirect(url_for('AccountRoute.index'))
                    else:
                        flash('CONTRASEÑA INCORRECTA', 'warning')
                        return render_template('/Account/SignIn.html', form = login_form)
                else:                
                    flash('USUARIO INCORRECTO', 'warning')
                    return render_template('/Account/SignIn.html', form = login_form)
            except:
                flash('BASE DE DATOS "DESCONECTADO"', 'danger')
                return render_template('/Account/SignIn.html', form = login_form)
        else:
            return render_template('/Account/SignIn.html', form = login_form)
        
    def Register(self):
        register_form = Forms.UsersForm(request.form)

        if request.method == 'POST':
            email = register_form.email.data
            user = db.session.query(Users).filter(Users.Email == email).first()
            if user is not None:
                flash('EL CORREO QUE INGRESO YA EXISTE', 'warning')
                return render_template('/Account/SignUp.html', form = register_form)
            else:
                if Users.query.first() is None:
                    role = Roles(Name = 'Manager')
                    db.session.add(role)
                    role = Roles(Name = 'Administrator')
                    db.session.add(role)
                    role = Roles(Name = 'Supervisor')
                    db.session.add(role)
                    role = Roles(Name = 'Cashier')
                    db.session.add(role)
                    role = Roles(Name = 'Client')
                    db.session.add(role)
                    db.session.commit()
                    role = Roles.query.filter_by(Name = 'Manager').first()
                    user = Users(register_form.name.data, register_form.ci.data, register_form.address.data,
                                register_form.phone.data, register_form.email.data, register_form.password.data)
                    db.session.add(user)
                    role.UserRole.append(user)
                    db.session.add(role)
                    db.session.commit()
                else:
                    role = Roles.query.filter_by(Name = 'Client').first()
                    user = Users(register_form.name.data, register_form.ci.data, register_form.address.data,
                                register_form.phone.data, register_form.email.data, register_form.password.data)
                    db.session.add(user)
                    role.UserRole.append(user)
                    db.session.add(role)
                    db.session.commit()
                name = register_form.name.data
                session['username'] = name
                session['email'] = register_form.email.data
                """ session['RoleId'] = role """
                flash('REGISTRO EXITOSO', 'success')
                return redirect(url_for('AccountRoute.index'))
        else:
            return render_template('/Account/SignUp.html', form = register_form)
        
    def Logout(self):
        if 'username' in session:
            session.pop('username', None)
            session.pop('email', None)
            flash('INICIE SESIÓN', 'warning')
        return redirect(url_for('AccountRoute.login'))


AccountController = AccountController()