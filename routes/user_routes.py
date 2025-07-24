from flask import Blueprint, request
from controllers.user_controller import UserController

user_bp = Blueprint('users', __name__)
user_controller = UserController()

@user_bp.route('/')
def home():
    return "User Management System"

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    return user_controller.get_all_users()

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return user_controller.create_user(data)

@user_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return user_controller.update_user(user_id, data)

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_controller.delete_user(user_id)

@user_bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    return user_controller.search_users(name)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return user_controller.login(data)