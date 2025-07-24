from flask import jsonify
from services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()
    
    def get_all_users(self):
        try:
            users = self.user_service.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def get_user(self, user_id):
        try:
            user = self.user_service.get_user_by_id(user_id)
            if user:
                return jsonify(user), 200
            else:
                return jsonify({"error": "User not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def create_user(self, data):
        try:
            user = self.user_service.create_user(data)
            return jsonify({"message": "User created successfully", "user": user}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def update_user(self, user_id, data):
        try:
            user = self.user_service.update_user(user_id, data)
            return jsonify({"message": "User updated successfully", "user": user}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def delete_user(self, user_id):
        try:
            self.user_service.delete_user(user_id)
            return jsonify({"message": "User deleted successfully"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def search_users(self, name):
        try:
            users = self.user_service.search_users(name)
            return jsonify(users), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def login(self, data):
        try:
            user = self.user_service.authenticate_user(data.get('email'), data.get('password'))
            if user:
                return jsonify({"status": "success", "user": user}), 200
            else:
                return jsonify({"status": "failed", "error": "Invalid credentials"}), 401
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500