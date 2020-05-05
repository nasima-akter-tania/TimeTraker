from main import db


#SUBJECT MODEL FOR DATABASE TABLE
class SubjectModel(db.Model):
    __tablename__ = 'subjects'
    
    p_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    code = db.Column(db.String(120), unique = True, nullable = False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.p_id', nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.p_id', nullable = False)
  
 
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
        return {
                'name': data.name,
                'code': data.code,
                'class':data.class_id,
                'department':data.department_id
                }
    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id = p_id).first()
        
    @classmethod
    def return_all(cls):
        return {'users': list(map(lambda x: self.to_json(x), SubjectModel.query.all()))}


