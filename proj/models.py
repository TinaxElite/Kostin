from database import db
from datetime import datetime


class ContactsInfo(db.Model):
    __tablename__ = 'contacts_info'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    fax_number = db.Column(db.String(20))
    email = db.Column(db.String(100))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    

    def __repr__(self) -> str:
        return f'{self.id}'


class Categories(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self) -> str:
        return f'{self.id}'
    
    
class Posts(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    id_category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    author = db.Column(db.String(100))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    img = db.Column(db.String(100))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f'{self.id}'
    
