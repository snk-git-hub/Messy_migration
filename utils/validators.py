import re

def validate_user_data(data):
    required_fields = ['name', 'email', 'password']
    return all(field in data and data[field] for field in required_fields)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None