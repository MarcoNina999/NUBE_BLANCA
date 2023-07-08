from app import db

ServiceSubservice = db.Table('service_subservice',
    db.Column('ServiceId', db.Integer, db.ForeignKey('services.Id'), primary_key=True),
    db.Column('SubserviceId', db.Integer, db.ForeignKey('subservices.Id'), primary_key=True)
)

class Services(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Name = db.Column(db.String(50), nullable = True)
    Description = db.Column(db.String(255), nullable = False)

    def __init__(self, Name, Description):
        self.Name = Name
        self.Description = Description