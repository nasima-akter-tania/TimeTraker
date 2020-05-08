from run import db


#STUDENT MODEL FOR DATABASE TABLE
class StudentModel(db.Model):
    __tablename__ = 'students'
    
    p_id = db.Column(db.Integer, primary_key = True)
    reg_no = db.Column(db.String(100), unique = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)
    gender = db.Column(db.String(120), nullable = False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.p_id'), nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.p_id'), nullable = False)
    session = db.Column(db.String(50), nullable = False)
    classes= db.relationship("ClassModel", backref=db.backref("std_class", uselist=False))
    departmentes = db.relationship("DepartmentModel", backref=db.backref("std_departments", uselist=False))
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()
    def db_to_commit(self):
        db.session.commit()

    @staticmethod
    def to_json(x):
        return {
                'reg_no': x.reg_no,
                'name': x.name,
                'gender':x.gender,
                'class_id':x.class_id,
                'department_id':x.department_id,
                'session':x.session
                }
    def update_data(self, old_data,new_data):
        old_data.reg_no = new_data['reg_no']
        old_data.name =  new_data['name']
        old_data.gender = new_data['gender']
        old_data.class_id = new_data['class_id']
        old_data.department_id = new_data['department_id']
        old_data.session = new_data['session']
       
        return old_data
    

    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id = p_id).first()

    @classmethod
    def find_by_reg(cls, reg_no):
        return cls.query.filter_by(reg_no = reg_no).first()
 
    @classmethod
    def return_all(cls):
        return {'students': list(map(lambda data: cls.to_json(data), StudentModel.query.all()))}


