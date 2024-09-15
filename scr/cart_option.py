from flask import jsonify,request
from model import PCart
from flask_sqlalchemy import SQLAlchemy


class CartOption:
    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db

    def get_Cart(self, p_id = None):
        pc = PCart.query
        if p_id:
            pc = pc.filter(PCart.id.__eq__(p_id))
        products = pc.all()
        return jsonify([p.to_dict() for p in products]) if len(products) else 'Khong thay san pham'
    
    def add_Cart(self,product_id = None):
        try:
            if not product_id:
                data = request.get_json()
                if not data or 'id' not in data:
                    return jsonify({"error": "Invalid input"}), 400
                
                product_id = data['id']
            pc = PCart.query.get(product_id)
            if pc:
                pc.num += 1
                self.db.session.commit()
                return jsonify({"message": f"Sản phẩm {product_id} đã thêm số lượng"}), 200
            else:
                prod = PCart(id=product_id)
                self.db.session.add(prod)
                self.db.session.commit()
                return jsonify({"message": "Sản phẩm đã thêm vào Giỏ hàng"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete_Cart(self,product_id = None):
        try:
            if not product_id:
                data = request.get_json()
                if not data or 'product_id' not in data:
                    return jsonify({"error": "Invalid input"}), 400
                
                product_id = data['product_id']
            item = PCart.query.get(product_id)
            if item:
                self.db.session.delete(item)
                self.db.session.commit()
                return jsonify({"message": f"Đã xóa sản phẩm có id = {product_id} khỏi giỏ hàng!"}), 200
            else:
                return jsonify({"error": "Sản phẩm không có trong Giỏ hàng"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
