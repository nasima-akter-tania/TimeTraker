from main import db


#ATTENDANCE MODEL FOR DATABASE TABLE
class AttendanceModel(db.Model):
    __tablename__ = 'std_attendance'
    
    p_id = db.Column(db.Integer, primary_key = True)   
    class_id = db.Column(db.Integer, db.ForeignKey('classes.p_id', nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.p_id'), nullable = False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.p_id'), nullable = False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.p_id'), nullable = False)
    status = db.Column(db.String(50), unique = True, nullable = False)

  
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()
    def db_to_commit(self):
        db.session.commit()
        
    #FOR CONVERT DATA INTO JSON FORMAT
    # @staticmethod
    # def to_json(data):
    #     return {
    #             'name': data.name,
    #             'code': data.code,
    #             'class':data.class_id,
    #             'department':data.department_id
    #             }
 
    # @classmethod
    # def return_all(cls):
    #     return {'users': list(map(lambda x: self.to_json(x), AttendanceModel.query.all()))}


