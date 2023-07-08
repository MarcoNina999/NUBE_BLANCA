from app import db
from app.Models.UsersModel import UserRole

class Roles(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Name = db.Column(db.String(50), nullable = True)

    UserRole = db.relationship('Users', secondary = UserRole, lazy='subquery', backref = db.backref('roles', lazy=True))