from flask.ext import restful

class APIMaster(restful.Resource):
    def get(self):
        return {"message":"method not implemented"}, 400

    def post(self):
        return {"message":"method not implemented"}, 400

    def put(self):
        return {"message":"method not implemented"}, 400

    def delete(self):
        return {"message":"method not implemented"}, 400