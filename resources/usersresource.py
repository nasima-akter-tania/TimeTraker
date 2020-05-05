from flask_restful import Resource, reqparse
from models.users import UserModel

from flask_jwt_extended import (create_access_token, 
                                create_refresh_token, jwt_required, 
                                jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt
                                )

parser = reqparse.RequestParser()
parser.add_argument('email', help = 'email field required', required = True)
parser.add_argument('password', help = 'password field required', required = True)


class EmployeeRegistration(Resource):
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



class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_email(data['email']) # GET USER DATA BY EMAIL

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['name'])}

        if UserModel.verify_hash(data['password'], current_user.password):
            return {'message': 'Logged in as {}'.format(current_user.name)}
        else:
            return {'message': 'Wrong credentials'}
      
class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

class UserBase(Resource):
    def get(self, p_id):
        user_data = UserModel.find_by_id(p_id)
        jsonify_data =user_data.to_json(user_data)
        return {'user': jsonify_data}
        
       
    def delete(self, p_id):
        user_data = UserModel.find_by_id(p_id)
        if user_data:
            user_data.db_to_delete()
            return {'message': 'user data deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 500
    def put(self, p_id):
        
        parser.add_argument('name', help = 'name filed required', required = True)
        parser.add_argument('phone', help = 'phone field required', required = True)
        parser.add_argument('gender', help = 'gender field required', required = True)
        parser.add_argument('designation', help = 'designation field required', required = True)
        parser.add_argument('role', help = 'role field required', required = True)
        data = parser.parse_args()
        user_data = UserModel.find_by_id(p_id)
        user_data.update_data(user_data,data)

        user_data.db_to_commit
        
     

        return {"ok":"success"}
       
       




      
