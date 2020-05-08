from flask_restful import Resource, reqparse
from models.classes import ClassModel
from flask_jwt_extended import jwt_required
                               
                                

parser = reqparse.RequestParser()
parser.add_argument('name', help = 'registration no field required', required = True)
parser.add_argument('code', help = 'name field required', required = True)



class ClassRegistration(Resource):
    """ this resource for this endpoint /add_class for save data into database"""
    @jwt_required
    def post(self):
        data = parser.parse_args()

        if ClassModel.find_by_name(data['name']):
            return {'message': 'This class {} already exists '. format(data['name'])}

        if ClassModel.find_by_code(data['code']):
            return {'message': 'This code {} already exists '. format(data['code'])}
        
        #CREATE MODEL DATA FOR SAVE 
        new_class = ClassModel(
                        name   = data['name'],
                        code   = data['code'],
                    )
        try:
            new_class.save_to_db() #CALL THIS FUNCTION FOR COMMIT DATA
          
            return {
                'message': ' This {} class data  created successfully'.format(data['name'])
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500




class AllClasses(Resource):
    """this resource for /classes endpoint by this url all classes data can view"""
    @jwt_required
    def get(self):
        return ClassModel.return_all()

class ClassBase(Resource):
    """this resource for /class/<int:p_id> endpoint by this url classes data can update, delete, single data view """
    @jwt_required
    def get(self, p_id):
        class_data = ClassModel.find_by_id(p_id) #GET SINGLE DATA BY ID
        jsonify_data = class_data.to_json(class_data)
        return {'class': jsonify_data}
        
    @jwt_required   
    def delete(self, p_id):
        class_data = ClassModel.find_by_id(p_id) #GET SINGLE DATA BY ID
        if class_data:
            class_data.db_to_delete()
            return {'message': 'Class data deleted successfully'}, 200
        else:
            return {'message': 'Class not found'}, 400
    @jwt_required
    def put(self, p_id):
        data = parser.parse_args()
        class_data = ClassModel.find_by_id(p_id)
        class_data.update_data(class_data,data)

        try:
            class_data.db_to_commit()
            return {
                'message': ' This {} class data  updated successfully'.format(data['name'])
            }, 200
        except:
            return {'message': 'Something went wrong'}, 500
       
        
     

       
       




      
