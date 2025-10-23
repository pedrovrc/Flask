"""
app.py: Application factory for Database_and_API project.
"""
from flask import Flask
from config import Config
from models import db
from api import api_bp
from web import web_bp
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db, directory=os.path.join(os.path.dirname(__file__), 'migrations'))
    app.register_blueprint(api_bp)
    app.register_blueprint(web_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)