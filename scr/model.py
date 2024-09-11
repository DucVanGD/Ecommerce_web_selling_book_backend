from db import db
from sqlalchemy import Integer, String, Column, Float, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    img = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    author = Column(String(50), nullable=False)
    detail = Column(String(200), nullable=True)
    ptype = Column(String(50), nullable=False)
    stock = Column(Integer, default=1)
    #pcarts = relationship('PCart', backref='product', lazy = True)




class PCart(Product):

    id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    date = Column(DATETIME, default=datetime.now)
    num = Column(Integer, default=1)
    product = relationship('Product', backref='pcarts', lazy = True)
    def to_dict(self):
        return {
            'id': self.id,
            'date':self.date,
            'num': self.num
        }

class User(db.Model):
    id = Column(Integer, primary_key= True, autoincrement= True)
    username = Column(String(100),nullable=  False, unique= True)
    password = Column(String(100),nullable=  False)
    email = Column(String(50),nullable=  True)
    phone = Column(String(20),nullable=  True)
    img = Column(String(100),nullable=  True)
    point = Column(Integer,nullable=  False, default= 0)
    birthday = Column(DATETIME,nullable=  False)
    gender = Column(String(10),nullable=  False)
    purchased = Column(Integer,nullable=  False, default= 0)
    donations = Column(Integer,nullable=  False, default= 0)
    role = Column(Integer,nullable=  False, default= 0) # 0 la user, 1 la admin
    def rank(self):
        pass
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email' : self.email,
            'phone' : self.phone,
            'img' : self.img,
            'point': self.point,
            'birthday': self.birthday,
            'gender': self.gender,
            'purchased': self.purchased,
            'donations': self.donations,
            'role': self.role
        }


