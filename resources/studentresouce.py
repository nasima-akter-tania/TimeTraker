from flask_restful import Resource, reqparse
from models.students import StudentModel

from flask_jwt_extended import jwt_required
                               
                                

parser = reqparse.RequestParser()
parser.add_argument('email', help = 'email field required', required = True)
parser.add_argument('password', help = 'password field required', required = True)


class StudentRegistration(Resource):
    def post(self):
        parser.add_argument('name', help = 'name filed required', required = True)
        parser.add_argument('phone', help = 'phone field required', required = True)
        parser.add_argument('gender', help = 'gender field required', required = True)
        parser.add_argument('designation', help = 'designation field required', required = True)
        parser.add_argument('role', help = 'role field required', required = True)
        
        data = parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {'message': 'User {} already exists with this {}'. format(data['name'],data['email'])}

        new_user = UserModel(
            name        = data['name'],
            email       = data['email'],
            password    = UserModel.generate_hash(data['password']), #FOR HASH PASSWORD CALL GENERATE HAS METHOD
            phone       = data['phone'],
            gender      = data['gender'],
            designation = data['designation'],
            role        =data['role']

        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['email'])
            return {
                'message': ' {} data created successfully'.format( data['name']),
                'access_token': access_token,

            }
        except:
            return {'message': 'Something went wrong'}, 500




class AllStudents(Resource):
    def get(self):
        return StudentModel.return_all()

class UserBase(Resource):
    def get(self, p_id):
        student_data = StudentModel.find_by_id(p_id)
        jsonify_data = student_data.to_json(student_data)
        return {'user': jsonify_data}
        
       
    def delete(self, p_id):
        student_data = StudentModel.find_by_id(p_id)
        if student_data:
            student_data.db_to_delete()
            return {'message': 'user data deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 500
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
       
       




      
