from APIExample import *
from Token import *
from Application import api

# ---------------------
# Add the API's address mappings.
# We are at v1 at the moment. This will allow us to implement new API's 
# later on if this needs to scale.

# Example Setup!
api.add_resource(APIExample, '/api/v1/example/')
api.add_resource(Token, '/api/v1/token/')
