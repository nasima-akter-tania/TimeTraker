from main import db


#CLASS MODEL FOR DATABASE TABLE
class ClassModel(db.Model):
    __tablename__ = 'classes'
    
    p_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable = False)
    code = db.Column(db.String(120), unique = True, nullable = False)
  
 
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
                }
    @classmethod
    def find_by_code(cls, code):
        return cls.query.filter_by(code = code).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()


    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id = p_id).first()
              
    @classmethod
    def return_all(cls):
        return {'classes': list(map(lambda x: cls.to_json(x), ClassModel.query.all()))}


