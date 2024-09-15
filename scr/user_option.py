from flask import jsonify,request
from model import User
from flask_sqlalchemy import SQLAlchemy
import hashlib
class User_option:
    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db
    def add_user(self):
        data = request.get_json()
        if not data: return jsonify({"error": "Invalid input"}), 400
        name,password,email,img = data['name'],data['password'],data['email'],img = data['img']
        birthday,gender, phone = data['birthday'], data['gender'],data['phone']
        repass = data['repass']
        
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        repass = str(hashlib.md5(repass.strip().encode('utf-8')).hexdigest())

        if repass != password:
            return jsonify('Mật khẩu nhập lại không giống nhau'),400
        user = User(name=name.strip(), password = password.strip(), email =email.strip(), img = img.strip(), 
                    birthday = birthday.strip(),gender = gender.strip(), phone = phone.strip()
                    )
        self.db.session.add(user)
        self.db.session.commit()
    def delete_user(self):
        data = request.get_json()
        if not data: return jsonify({"error": "Invalid input"}), 400
        user = User.query.get(data['id'])
        if user:
            self.db.session.delete(user)
            self.db.session.commit()
            return jsonify({"message": f"Đã xóa tài khoản của bạn!"}), 200
        else:
            return jsonify({"error": "Người dùng không tồn tại"}), 404
    def login(self):
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        email = data['email']
        password = data['password']

        if not email or not password:
            return jsonify({"error": "Thiếu thông tin đăng nhập"}), 400
        
        user = User.query.filter((User.email.__eq__(email))).first()
        if not user:
            return jsonify({"error": "Tài khoản không chính xác"}), 404
        if user.password != password: 
            return jsonify({"error": "Mật khẩu không chính xác"}), 401
        
        return jsonify(user.to_dict()), 200

        
