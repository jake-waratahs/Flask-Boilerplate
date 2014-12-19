from flask.ext.security import auth_token_required
from .APIMaster import APIMaster
from Application import api

class APIExample(APIMaster):
    def get(self):
        return {"message":"method not implemented"}, 400

    # Force Auth Token
    @auth_token_required
    def post(self):
        return {"message":"method not implemented"}, 400

    def put(self):
        return {"message":"method not implemented"}, 400

    def delete(self):
        return {"message":"method not implemented"}, 400

api.add_resource(APIExample, '/api/v1/example/')