from flask.ext import restful
from flask.ext.restful import reqparse
from Application import api
from Application.models import *
from flask.ext.security import auth_token_required, roles_required
from APIMaster import APIMaster

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