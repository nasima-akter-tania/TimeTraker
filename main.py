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

from  resources import usersresource, studentresouce, classresource, departmentresource
from models import users
# import views

#TEACHERS END POINT'S 
api.add_resource(usersresource.EmployeeRegistration, '/registration')
api.add_resource(usersresource.UserLogin, '/login')
api.add_resource(usersresource.AllUsers, '/teachers')
api.add_resource(usersresource.UserBase, '/teacher/<int:p_id>')

#STUDENT END POINT'S 
# api.add_resource(studentresouce.StudentRegistration, '/student_add')
# api.add_resource(studentresouce.StudentRegistration, '/students')
# api.add_resource(studentresouce.StudentRegistration, '/student/<int:p_id>')

#CLASS END POINT'S 
api.add_resource(classresource.ClassRegistration, '/class_add')
api.add_resource(classresource.AllClasses, '/classes')
api.add_resource(classresource.ClassBase, '/class/<int:p_id>')


#DEPARTMENT END POINT'S 
api.add_resource(departmentresource.DepartmentRegistration, '/department_add')
api.add_resource(departmentresource.AllDepartments, '/departments')
api.add_resource(departmentresource.DepartmentBase, '/department/<int:p_id>')

#SUBJECTS END POINT'S 
# api.add_resource(subject_add.StudentRegistration, '/subject_add')
# api.add_resource(studentresouce.AllSubjects, '/subjects')
# api.add_resource(studentresouce.SubjectBase, '/subject/<int:p_id>')
