from flask import jsonify,json
from model import Product, PCart
from flask_sqlalchemy import SQLAlchemy


class CartOption:
    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db

    def get_Cart(self, p_id = None, p_name=None):
        pc = PCart.query
        if p_id:
            pc = pc.filter(PCart.id.__eq__(p_id))
        if p_name:
            pc = pc.filter(PCart.name.__eq__(p_name))
        products = pc.all()
        return jsonify([p.to_dict() for p in products]) if len(products) else 'Khong thay san pham'
    
    def add_Cart(self, product_id):
        pc = PCart.query.get(product_id)
        if pc:
            pc.num+=1
        else: 
            product = Product.query.get(product_id)
            prod = PCart(name = product.name, id = product.id,
                        img = product.img, price = product.price,
                        detail = product.detail, ptype = product.ptype,
                        author = product.author
                        )
            self.db.session.add(prod)
            self.db.session.commit()  

    @classmethod
    def delete_Cart(self, product_id):
        item = PCart.query.get(product_id)
        if item:
            self.db.session.delete(item)
            self.db.session.commit()
