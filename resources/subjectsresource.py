from flask_restful import Resource, reqparse
from models.subjects import SubjectModel
from flask_jwt_extended import jwt_required
                               
                                

parser = reqparse.RequestParser()
parser.add_argument('name', help = 'name field required', required = True)
parser.add_argument('code', help = 'code field required', required = True)
parser.add_argument('class_id', help = 'class field required', required = True)
parser.add_argument('department_id', help = 'department field required', required = True)


class SubjectRegistration(Resource):
    @jwt_required
    def post(self):
        data = parser.parse_args()

        if SubjectModel.find_by_name(data['name']):
            return {'message': 'This subject {} already exists '. format(data['name'])}

        if SubjectModel.find_by_code(data['code']):
            return {'message': 'This code {} already exists '. format(data['code'])}

        new_subject = SubjectModel(
                        name               = data['name'],
                        code               = data['code'], 
                        class_id           = data['class_id'],
                        department_id      = data['department_id'],
                      
                )
        try:
            new_subject.save_to_db()
          
            return {
                'message': 'Subject {} data created successfully'.format( data['name'])

            }, 200
        except:
            return {'message': 'Something went wrong'}, 400




class AllSubjects(Resource):
    """this resource for /students endpoint by this url all students data can view"""
    @jwt_required
    def get(self):
        return SubjectModel.return_all()

class SubjectBase(Resource):
    @jwt_required
    def get(self, p_id):
        subject_data = SubjectModel.find_by_id(p_id)
        jsonify_data = subject_data.to_json(subject_data)
        return {'subject': jsonify_data}
        
    @jwt_required   
    def delete(self, p_id):
        subject_data = SubjectModel.find_by_id(p_id)
        if subject_data:
            subject_data.db_to_delete()
            return {'message': 'Subject data deleted successfully'}, 200
        else:
            return {'message': 'Subject not found'}, 400
    @jwt_required        
    def put(self, p_id):
        data = parser.parse_args()
        subject_data = SubjectModel.find_by_id(p_id)
        subject_data.update_data(subject_data,data)
        try:
            subject_data.db_to_commit()
            return {
                'message': ' This {} subject data  updated successfully'.format(data['name'])
            }, 200

        except:
            return {'message': 'Something went wrong'}, 500
           
        
     

       
       
       




      
