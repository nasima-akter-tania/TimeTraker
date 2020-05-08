from run import db
from models.classes import ClassModel
from models.students import StudentModel

#ATTENDANCE MODEL FOR DATABASE TABLE
class AttendanceModel(db.Model):
    __tablename__ = 'std_attendance'
    
    p_id = db.Column(db.Integer, primary_key = True)  
    date = db.Column(db.DateTime(), nullable=False) 
    class_id = db.Column(db.Integer, db.ForeignKey('classes.p_id'), nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.p_id'), nullable = False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.p_id'), nullable = False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.p_id'), nullable = False)
    status = db.Column(db.String(50), nullable = False)
    classes= db.relationship("ClassModel", backref=db.backref("atten_class", uselist=False))
    departmentes = db.relationship("DepartmentModel", backref=db.backref("atten_class", uselist=False))
    subjects = db.relationship("SubjectModel", backref=db.backref("atten_subject"))
    students = db.relationship("StudentModel", backref=db.backref("atten_student"))
    
  
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()
    def db_to_commit(self):
        db.session.commit()
    

    #FOR CONVERT DATA INTO JSON FORMAT
    @staticmethod
    def to_json(data):
        date = data.date
        return {
                'date': date.strftime("%Y-%m-%d"),
                'class': data.class_id,
                'department': data.department_id,
                'subject': data.subject_id,
                'student' : data.student_id,
                'status': data.status
      
             }
    @classmethod 
    def find_by_date(cls, class_id, department_id, subject_id, date ):
         return AttendanceModel.query.filter_by(class_id = class_id, department_id= department_id, subject_id=subject_id, date = date).first()
   
    @classmethod 
    def find_student_by_reg(cls, student_id):
         return StudentModel.query.filter_by(student_id = student_id).first()

    @classmethod
    def return_all(cls, class_id, department_id, subject_id, date):
        print(date)
        return {'attendance': list(map(lambda x: cls.to_json(x), AttendanceModel.query.filter_by( date = date,class_id = class_id, department_id= department_id, subject_id=subject_id).all()))}


