from main import db
from passlib.hash import pbkdf2_sha256 as sha256


#TEACHER MODEL NAME AS USERS
class UserModel(db.Model):
    __tablename__ = 'users'
    
    p_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    gender = db.Column(db.String(20), nullable = False)
    designation = db.Column(db.String(50), nullable = False)
    role = db.Column(db.String(50), nullable = False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def db_to_delete(self):
        db.session.delete(self)
        db.session.commit()
    def db_to_commit(self):
        db.session.commit()

   
    def update_data(self, old_data,new_data):
        old_data.name = new_data['name']
        old_data.email =  new_data['email']
        old_data.password = new_data['password']
        old_data.phone = new_data['phone']
        old_data.gender = new_data['gender']
        old_data.designation = new_data['designation']
        old_data.role = new_data['role']
       
        return old_data
    
    @staticmethod
    def to_json(data):
        return {
                'name': data.name,
                'email': data.email,
                'password':data.password,
                'phone':data.phone,
                'gender':data.gender,
                'designation':data.designation,
                'role':data.role
               
                }  
         
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()
    @classmethod
    def find_by_id(cls, p_id):
        return cls.query.filter_by(p_id = p_id).first()
 
    @classmethod
    def return_all(cls):   
        return {'users': list(map(lambda user: cls.to_json(user), UserModel.query.all()))}
      


