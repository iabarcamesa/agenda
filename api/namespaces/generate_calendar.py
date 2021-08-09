from flask import request
from flask_restx import Namespace, Resource, fields, cors, reqparse

from app.interactors.generate_calendar import GenerateCalendar

from api.authentication import decode_vat

ns = Namespace('generate_calendar',
               description='Description')


@ns.route('')
class GenerateCalendarEndpoint(Resource):

    @cors.crossdomain(origin='*')
    @ns.param('year', 'Year', type=int, default='2021')
    @ns.param('month', 'Month', type=int, default='10')
    def get(self):
  
        try:
            data = GenerateCalendar(month=int(request.args['month']), 
                                   year=int(request.args['year']), 
                                   practitioner=decode_vat(request)).execute()
            return data
        except Exception as e:
            return str(e), 400

    def options(self):
        return {'Allow': 'GET'}, 200, \
            {'Access-Control-Allow-Origin': '*',
             'Access-Control-Allow-Methods': 'GET',
             "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
             }
