from flask import Flask
from myapp.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt_manager = JWTManager()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt_manager.init_app(app)

    from myapp.models import Student, Course
    from myapp.auth.routes import auth
    from myapp.errors.routes import error
    from myapp.stundents.routes import student 
    from myapp.courses.routes import course

    app.register_blueprint(auth,url_prefix="/api/auth")
    app.register_blueprint(course,url_prefix="/api")
    app.register_blueprint(student,url_prefix="/api")
    app.register_blueprint(error)


    return app