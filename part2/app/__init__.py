from flask import Flask
from flask_restx import Api

from app.api.v1.users import api as users_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.amenities import api as amenities_ns
#from app.api.v1.places import api as places_ns  #added
#from app.api.v1.amenities import api as amenities_ns  #added
#from app.api.v1.reviews import api as reviews_ns  #added

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API')

    # Enregistrement des namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    return app
    #api.add_namespace(places_ns, path='/api/v1/places')  #added
    #api.add_namespace(amenities_ns, path='/api/v1/amenities')  #added
    #api.add_namespace(reviews_ns, path='/api/v1/reviews')  #added

    return app
