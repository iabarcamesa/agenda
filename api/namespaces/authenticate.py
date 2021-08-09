from flask import request
from flask_restx import Namespace, Resource, fields, cors

from api.authentication import account_does_not_exists, password_is_not_valid, generate_token

ns = Namespace('authentication', description='Autentication endpoint')

authorization = ns.model('Authorization', {
    'vat': fields.String(required=True, description='The vat for authentication'),
    'password': fields.String(required=True, description='The password for authentication'),
})


@ns.route('')
class Authenticate(Resource):

    @ns.expect(authorization)
    @cors.crossdomain(origin='*')
    @ns.doc(security=[])
    def post(self):
        '''Get authentication token'''

        if account_does_not_exists(request) or password_is_not_valid(request):
            return {
                    "success": False,
                    "message": "User not authenticated"
                   }, 401
        else:
            return {
                    "success": True,
                    "message": "Authentication successful",
                    "token": generate_token(request)
                   }, 200

    @ns.doc(security=[])
    def options(self):
        return {'Allow': 'POST'}, 200, \
               {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST',
                "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
                }
