from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.Models.AcquireModel import Acquire

UserRole = db.Table('user_role',
    db.Column('UserId', db.Integer, db.ForeignKey('users.Id'), primary_key=True),
    db.Column('RoleId', db.Integer, db.ForeignKey('roles.Id'), primary_key=True)
)

class Users(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Name = db.Column(db.String(50), nullable = True)
    CI = db.Column(db.Integer, nullable = True)
    Address = db.Column(db.String(50), nullable = True)
    Phone = db.Column(db.Integer, nullable = True)
    Email = db.Column(db.String(50), nullable = True)
    Password =db.Column(db.String(255), nullable = True)

    Acquire = db.relationship('Acquire', backref='users', lazy=True)

    def __init__(self, Name, CI, Address, Phone, Email, Password):
        self.Name = Name
        self.CI = CI
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Password = self.__create_password__(Password)

    def __create_password__(self, Password):
        return generate_password_hash(Password)
    
    def __verify_passwrod__(self, Password):
        return check_password_hash(self.Password, Password)