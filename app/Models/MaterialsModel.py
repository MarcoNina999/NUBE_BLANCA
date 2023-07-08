from app import db
from datetime import datetime

class Materials(db.Model):
    Id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Name = db.Column(db.String(50), nullable = True)
    Quantity = db.Column(db.Integer, default = 0, nullable = False)
    Create_at = db.Column(db.DateTime, index = True, default = datetime.now)
    is_active = db.Column(db.Boolean, default = True)

    def __init__(self, Name, Quantity, Create_at, is_active):
        self.Name = Name
        self.Quantity = Quantity
        self.Create_at = Create_at
        self.is_active = is_active