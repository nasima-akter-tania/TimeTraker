from flask_restful import Resource, reqparse
from models.attendance import AttendanceModel
from flask_jwt_extended import jwt_required
import datetime                              
                                

parser = reqparse.RequestParser()
parser.add_argument('date', help = 'date  field required', required = True)
parser.add_argument('class_id', help = 'class field required', required = True)
parser.add_argument('department_id', help = 'department field required', required = True)
parser.add_argument('subject_id',help = 'subject field required', required = True)

class AttendanceTake(Resource):
    """ this resource for this endpoint /attendance_add for take attendance and save attendance data into database"""
    @jwt_required
    def post(self):
        parser.add_argument('present_student', type=int, action = "append", help = 'student field required', required = True)
        parser.add_argument('absant_student', type=int, action = "append", help = 'student field required', required = True)

        data = parser.parse_args()

        student_attendance = [] 
        y, m, d = data['date'].split('-')
        class_date = datetime.datetime(int(y), int(m), int(d))
        
        if AttendanceModel.find_by_date(data['class_id'], data['department_id'], data['subject_id'], class_date):
            return {'message': 'This date {} data already exists '. format(data['date'])}
       
       
  
        present_data_add =  [student_attendance.append({
                                "date": class_date,
                                "class_id":data['class_id'],
                                "department_id":data['department_id'],
                                "subject_id":data['subject_id'],
                                "student_id":p_data,
                                "status": "Present",

                            }) for p_data in data['present_student'] ]
        present_data_add =  [student_attendance.append({
                                "date": class_date,
                                "class_id":data['class_id'],
                                "department_id":data['department_id'],
                                "subject_id":data['subject_id'],
                                "student_id":p_data,
                                "status": "Absent",

                            }) for p_data in data['absant_student' ]]
       
       
        try:
            for atten_data in student_attendance:
                add_attendance = AttendanceModel(**atten_data) #CREATE MODEL DATA FOR SAVE
                add_attendance.save_to_db()   #CALL THIS FUNCTION FOR COMMIT DATA
                    
            return {
                    'message': 'Attendance data added successfully'
                }, 200

               
        except:
            return {'message': 'Something went wrong'}, 500




class AllAttendance(Resource):
    """this resource for /classes endpoint by this url all classes data can view"""
    @jwt_required
    def post(self):
        data = parser.parse_args()
        y, m, d = data['date'].split('-')
        class_date = datetime.datetime(int(y), int(m), int(d))
        return AttendanceModel.return_all(data['class_id'], data['department_id'], data['subject_id'], class_date)


       




      
