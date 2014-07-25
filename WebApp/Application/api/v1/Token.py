from flask.ext import restful
from flask.ext.restful import reqparse
from Application import api
from Application.models import *
from flask.ext.security import auth_token_required, roles_required, http_auth_required
from APIMaster import APIMaster

class Token(APIMaster):
    @http_auth_required
    def get(self):
        user = current_user
        token = current_user.get_auth_token()
        return [{"token":token, 
                    "id": user.id, "email": user.email,
                    "isAdmin": user.isAdmin()}]


    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        args = parser.parse_args()

        if args.username is "":
            return {"message":"Username was not provided."}, 400

        if args.password is "":
            return {"message":"Password was not provided."}, 400


        user = app.user_datastore.get_user(args.username)
        if not user:
            return {"message":"Invalid Credentials"}, 400



        if (verify_password(args.password, user.password)):
            token = user.get_auth_token()
            return [{"token":token, 
                    "id": user.id, "email": user.email,
                    "isAdmin": user.isAdmin()}]

        else:
            # User isn't valid.
            return {"message":"Invalid Credentials"}, 400
