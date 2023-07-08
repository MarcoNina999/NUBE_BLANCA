from app import db
from datetime import datetime

class Acquire(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    UsersId = db.Column(db.Integer, db.ForeignKey('users.Id', ondelete="CASCADE"), nullable = False)
    ServicesId = db.Column(db.Integer, db.ForeignKey('services.Id', ondelete="CASCADE"), nullable = False)
    Subservices = db.Column(db.String(255), nullable = True)
    Create_at = db.Column(db.DateTime, index = True, default = datetime.now, nullable = False)
    Total = db.Column(db.Float, default = 0, nullable = False)

    def __init__(self, UserId, ServicesId, Subservices, Total):
        self.UsersId = UserId
        self.ServicesId = ServicesId
        self.Subservices = Subservices
        self.Total = Total