from app import db

class Farmer(db.Model):
    " Create a Former table "

    __tablename__ = 'farmers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Farmer: {}>'.format(self.username)

def load_farmer(user_id):
    return Farmer.query.get(int(user_id))

class Farm(db.Model):
    " Create a  Farm table"

    __tablename__ = 'farms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    location = db.Column(db.String(120), unique=True)
    total_field_area = db.Column(db.Integer)
    average_temperature = db.Column(db.Integer)
    farmers = db.relationship('Farmer', backref='farm', lazy='dynamic')
    
    def __repr__(self):
        return '<Farm: {}>'.format(self.name)

class Role(db.Model):
    " Create a Role table. "

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    farmers = db.relationship('Farmer', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)