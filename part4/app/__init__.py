from flask import Flask, jsonify
from flask_restx import Api
from werkzeug.exceptions import BadRequest
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

from app.api.v1.users import api as users_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.auth import api as auth_ns  ###
from app.api.v1.admin import api as admin_ns


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:5000", "http://127.0.0.1:5000",
                       "http://localhost", "http://127.0.0.1",
                       "http://localhost:5500", "http://127.0.0.1:5500"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "Accept"],
            "supports_credentials": True
        }
    })

    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        response = jsonify({
            "error ": str(error)
        })
        response.status_code = 400
        return response

    # Enregistrement des namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(auth_ns, path='/api/v1/auth') ###
    api.add_namespace(admin_ns, path="/api/v1/admin")
    return app