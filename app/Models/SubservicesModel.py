from app import db
from app.Models.ServicesModel import ServiceSubservice

class Subservices(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Name = db.Column(db.String(50), nullable = True)
    Description = db.Column(db.String(255), nullable = False)
    Price = db.Column(db.Float, default = 0, nullable = True)

    ServiceSubservice = db.relationship('Services', secondary = ServiceSubservice, lazy='subquery', backref = db.backref('subservices', lazy=True))

    def __init__(self, Name, Description, Price):
        self.Name = Name
        self.Description = Description
        self.Price = Price