from flask import request, jsonify, Blueprint, current_app
acc_route = Blueprint('acc_route', __name__)

@acc_route.route('/account', defaults={'user_id': None}, methods=['GET', 'POST', 'DELETE'])
@acc_route.route('/account/<user_id>', methods=['get'])
def data_user(user_id = None):
    if not user_id: 
        return 'Hãy đăng nhập vào tài khoản của bạn'
    return current_app.config['AccOption'].getin4()
@acc_route.route('/account/register', methods=['post'])
def regester():
    return current_app.config['AccOption'].add_user()