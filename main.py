from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timetraker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

from  resources import usersresource
from models import users

api.add_resource(usersresource.EmployeeRegistration, '/registration')
api.add_resource(usersresource.UserLogin, '/login')
api.add_resource(usersresource.AllUsers, '/teachers')
api.add_resource(usersresource.UserBase, '/teacher/<int:p_id>')


