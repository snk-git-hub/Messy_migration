from models.database import Database

class User:
    def __init__(self):
        self.db = Database()
    
    def get_all(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()
        conn.close()
        return users
    
    def get_by_id(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    def create(self, name, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id
    
    def update(self, user_id, name, email):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (name, email, user_id)
        )
        affected_rows = cursor.rowcount
        conn.commit()
        conn.close()
        return affected_rows > 0
    
    def delete(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        affected_rows = cursor.rowcount
        conn.commit()
        conn.close()
        return affected_rows > 0
    
    def search_by_name(self, name):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", (f'%{name}%',))
        users = cursor.fetchall()
        conn.close()
        return users
    
    def authenticate(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()
        return user