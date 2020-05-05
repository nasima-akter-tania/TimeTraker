from main import db


#STUDENT MODEL FOR DATABASE TABLE
class StudentModel(db.Model):
    __tablename__ = 'students'
    
    p_id = db.Column(db.Integer, primary_key = True)
    reg_no = db.Column(db.String(100), unique = True, nullable = False)
    name = db.Column(db.String(120), nullable = False)
    gender = db.Column(db.String(120), nullable = False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.p_id', nullable = False)
    department_id =  db.Column(db.Integer, db.ForeignKey('deparments.p_id', nullable = False)
    classes= relationship("ClassModel", backref=backref("classes", uselist=False))
    departmentes = relationship("DepartmentModel", backref=backref("departments", uselist=False))
    session = db.Column(db.String(50), nullable = False)

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
                'reg': x.reg,
                'name': x.name,
                'gender':x.gender,
                'class':x.classes.name,
                'department':x.departmentes.name,
                 'session':x.session
                }
    # def update_data(self, old_data,new_data):
    #     old_data.name = new_data['name']
    #     old_data.email =  new_data['email']
    #     old_data.password = new_data['password']
    #     old_data.phone = new_data['phone']
    #     old_data.gender = new_data['gender']
    #     old_data.designation = new_data['designation']
    #     old_data.role = new_data['role']
       
    #     return old_data
    

    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id = p_id).first()
 
    @classmethod
    def return_all(cls):
        return {'users': list(map(lambda x: self.to_json(x), StudentModel.query.all()))}


