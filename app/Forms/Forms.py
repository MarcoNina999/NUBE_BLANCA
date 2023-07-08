from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField, FloatField, FileField, StringField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import validators

class UsersForm(Form):
    name = StringField('Nombre', [DataRequired(message=('Nombre Requerido')), Length(min= 4, max=10)])
    ci = IntegerField('C.I.', [DataRequired(message=('CI Requerido')), Length(min=5, max=10)])
    address = StringField('Direcciónn', [DataRequired(message=('Dirección Requerido')), Length(max=64)])
    phone = IntegerField('Celular', [DataRequired(), Length(min=5, max=10)])
    email = StringField('Email', [DataRequired(message=('Email Requerido')), Email(message=('Email No Valido'))])
    password = PasswordField('Contraseña', [DataRequired()])
    confirmpassword = PasswordField('Confirmar Contraseña', [DataRequired(), EqualTo(password)])
    role = SelectField('roles')

class ServicesForm(Form):
    name = StringField('Servicio', [DataRequired(message=('Nombre Requerido')), Length(min= 4, max=30)])
    description = StringField('Descripcion', [DataRequired(message=('Descripción Requerido')), Length(min= 4, max=60)])
    price = FloatField('Precio', [DataRequired(message=('Nombre Requerido'))])