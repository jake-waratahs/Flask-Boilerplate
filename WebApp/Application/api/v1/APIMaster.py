from flask.ext import restful
from flask.ext.restful import reqparse
from Application import api
from Application.models import *
from flask.ext.security import auth_token_required, roles_required

class APIMaster(restful.Resource):
    def get(self):
        return {"message":"method not implemented"}, 400

    def post(self):
        return {"message":"method not implemented"}, 400

    def put(self):
        return {"message":"method not implemented"}, 400

    def delete(self):
        return {"message":"method not implemented"}, 400