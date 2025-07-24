from models.user import User
from utils.validators import validate_user_data, validate_email

class UserService:
    def __init__(self):
        self.user_model = User()
    
    def get_all_users(self):
        users = self.user_model.get_all()
        return [{"id": user[0], "name": user[1], "email": user[2]} for user in users]
    
    def get_user_by_id(self, user_id):
        user = self.user_model.get_by_id(user_id)
        if user:
            return {"id": user[0], "name": user[1], "email": user[2]}
        return None
    
    def create_user(self, data):
        if not validate_user_data(data):
            raise ValueError("Invalid user data")
        
        if not validate_email(data['email']):
            raise ValueError("Invalid email format")
        
        user_id = self.user_model.create(data['name'], data['email'], data['password'])
        return {"id": user_id, "name": data['name'], "email": data['email']}
    
    def update_user(self, user_id, data):
        if not data.get('name') or not data.get('email'):
            raise ValueError("Name and email are required")
        
        if not validate_email(data['email']):
            raise ValueError("Invalid email format")
        
        success = self.user_model.update(user_id, data['name'], data['email'])
        if not success:
            raise ValueError("User not found")
        
        return self.get_user_by_id(user_id)
    
    def delete_user(self, user_id):
        success = self.user_model.delete(user_id)
        if not success:
            raise ValueError("User not found")
        return True
    
    def search_users(self, name):
        if not name:
            raise ValueError("Name parameter is required")
        
        users = self.user_model.search_by_name(name)
        return [{"id": user[0], "name": user[1], "email": user[2]} for user in users]
    
    def authenticate_user(self, email, password):
        if not email or not password:
            raise ValueError("Email and password are required")
        
        user = self.user_model.authenticate(email, password)
        if user:
            return {"id": user[0], "name": user[1], "email": user[2]}
        return None