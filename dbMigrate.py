from app import db
from app.Models.AcquireModel import Acquire
from app.Models.MaterialsModel import Materials
from app.Models.RolesModel import Roles
from app.Models.ServicesModel import Services
from app.Models.SubservicesModel import Subservices
from app.Models.UsersModel import Users, UserRole

db.drop_all()
db.create_all()