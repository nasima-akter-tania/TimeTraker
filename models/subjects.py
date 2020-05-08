from run import db


#SUBJECT MODEL FOR DATABASE TABLE
class SubjectModel(db.Model):
    __tablename__ = 'subjects'
    
    p_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    code = db.Column(db.String(120), unique = True, nullable = False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.p_id'), nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.p_id'), nullable = False)
    classes= db.relationship("ClassModel", backref=db.backref("sub_class", uselist=False))
    departmentes = db.relationship("DepartmentModel", backref=db.backref("sub_class", uselist=False))
    
 
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()
    def db_to_commit(self):
        db.session.commit()

    def update_data(self, old_data,new_data):
        old_data.name =  new_data['name']
        old_data.code = new_data['code']
        old_data.class_id = new_data['class_id']
        old_data.department_id = new_data['department_id']
      
       
        return old_data
        
    #FOR CONVERT DATA INTO JSON FORMAT
    @staticmethod
    def to_json(data):
        return {
                'name': data.name,
                'code': data.code,
                'class':data.classes.name,
                'department':data.departmentes.name
                }
    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id = p_id).first()

    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code = code).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    @classmethod
    def return_all(cls):
        return {'subjects': list(map(lambda x: cls.to_json(x), SubjectModel.query.all()))}


