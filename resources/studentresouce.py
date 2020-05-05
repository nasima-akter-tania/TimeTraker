from flask_restful import Resource, reqparse
from models.students import StudentModel

from flask_jwt_extended import jwt_required
                               
                                

parser = reqparse.RequestParser()
parser.add_argument('reg_no', help = 'registration number field required', required = True)
parser.add_argument('name', help = 'name field required', required = True)
parser.add_argument('gender', help = 'gender filed required', required = True)
parser.add_argument('class_id', help = 'class field required', required = True)
parser.add_argument('department_id', help = 'department field required', required = True)
parser.add_argument('session', help = 'session field required', required = True)


class StudentRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if StudentModel.find_by_reg(data['reg_no']):
            return {'message': 'Student {} already exists with {} Registration'. format(data['name'],data['reg_no'])}

        new_student = StudentModel(
                        reg_no             = data['reg_no'],
                        name               = data['name'],
                        gender             = data['gender'], 
                        class_id           = data['class_id'],
                        department_id      = data['department_id'],
                        session            = data['session'],
                )
        try:
            new_student.save_to_db()
          
            return {
                'message': 'Student {} data created successfully'.format( data['name'])

            }, 200
        except:
            return {'message': 'Something went wrong'}, 500




class AllStudents(Resource):
    """this resource for /students endpoint by this url all students data can view"""
    def get(self):
        return StudentModel.return_all()

class StudentBase(Resource):
    def get(self, p_id):
        student_data = StudentModel.find_by_id(p_id)
        jsonify_data = student_data.to_json(student_data)
        return {'student': jsonify_data}
        
       
    def delete(self, p_id):
        student_data = StudentModel.find_by_id(p_id)
        if student_data:
            student_data.db_to_delete()
            return {'message': 'Student data deleted successfully'}, 200
        else:
            return {'message': 'Student not found'}, 500
    # def put(self, p_id):
        
    #     parser.add_argument('name', help = 'name filed required', required = True)
    #     parser.add_argument('phone', help = 'phone field required', required = True)
    #     parser.add_argument('gender', help = 'gender field required', required = True)
    #     parser.add_argument('designation', help = 'designation field required', required = True)
    #     parser.add_argument('role', help = 'role field required', required = True)
    #     data = parser.parse_args()
    #     student_data = StudentModel.find_by_id(p_id)
    #     student_data.update_data(student_data,data)

    #     student_data.db_to_commit
        
     

    #     return {"ok":"success"}
       
       




      
