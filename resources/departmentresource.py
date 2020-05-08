from flask_restful import Resource, reqparse
from models.departments import DepartmentModel
from flask_jwt_extended import jwt_required
                               
                                

parser = reqparse.RequestParser()
parser.add_argument('name', help = 'registration no field required', required = True)
parser.add_argument('code', help = 'name field required', required = True)
parser.add_argument('class_id', help = 'class field required', required = True)



class DepartmentRegistration(Resource):
    """ this resource for this endpoint /add_department for save data into database"""
    def post(self):
        data = parser.parse_args()

        if DepartmentModel.find_by_name(data['name']):
            return {'message': 'This department {} already exists '. format(data['name'])}

        if DepartmentModel.find_by_code(data['code']):
            return {'message': 'This code {} already exists '. format(data['code'])}
        
        #CREATE MODEL DATA FOR SAVE 
        new_department = DepartmentModel(
                        name        = data['name'],
                        code        = data['code'],
                        class_id    = data['class_id'],
                    )
        try:
            new_department.save_to_db() #CALL THIS FUNCTION FOR COMMIT DATA
          
            return {
                'message': ' This {} department data  created successfully'.format(data['name'])
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500




class AllDepartments(Resource):
    """this resource for /departments endpoint by this url all classes data can view"""
    def get(self):
        return DepartmentModel.return_all()

class DepartmentBase(Resource):
    """this resource for /department/<int:p_id> endpoint by this url classes data can update, delete, single data view """
    @jwt_required
    def get(self, p_id):
        department_data = DepartmentModel.find_by_id(p_id) #GET SINGLE DATA BY ID
        jsonify_data = department_data.to_json(department_data)
        return {'department': jsonify_data}
        
    @jwt_required   
    def delete(self, p_id):
        department_data = DepartmentModel.find_by_id(p_id) #GET SINGLE DATA BY ID
        if department_data:
            department_data.db_to_delete()
            return {'message': 'Department data deleted successfully'}, 200
        else:
            return {'message': 'Department not found'}, 400
    @jwt_required
    def put(self, p_id):
        data = parser.parse_args()
        department_data = DepartmentModel.find_by_id(p_id)
        department_data.update_data(department_data,data)

        try:
            department_data.db_to_commit()
            return {
                'message': ' This {} department data  updated successfully'.format(data['name'])
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500
        
     

       
       




      
