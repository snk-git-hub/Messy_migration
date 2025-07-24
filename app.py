from flask import Flask
from routes.user_routes import user_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)