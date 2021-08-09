from flask import request
from flask_restx import Namespace, Resource, fields, cors, reqparse
from datetime import datetime

from app.interactors.create_appointments import CreateAppointments

from api.authentication import decode_vat

ns = Namespace('create_appointment',
               description='Description')


@ns.route('')
class CreateAppointmentEndpoint(Resource):

    @cors.crossdomain(origin='*')
    @ns.param('date_time', '', type=str, default='2020-12-02 12:00')
    @ns.param('cost', 'Amount to add', type=int, default='10')
    @ns.param('patient', 'Amount to add', type=str, default='patient_1')
    @ns.param('every_number_of_weeks', 'Amount to add', type=int, default='1')
    @ns.param('repeat_until', 'Amount to add', type=str, default='2020-12-31')
    def post(self):
        '''Get data'''

        try:
            CreateAppointments(
                date_time = datetime.strptime(request.args['date_time'], '%Y-%m-%d %H:%M'),
                cost = int(request.args['cost']),
                practitioner = decode_vat(request),
                patient = request.args['patient'],
                every_number_of_weeks = int(request.args['every_number_of_weeks']),
                repeat_until = datetime.strptime(request.args['repeat_until'], '%Y-%m-%d')
            ).execute()
            return {'data': 'Appointments created'}
        except Exception as e:
            return str(e), 400

    def options(self):
        return {'Allow': 'GET'}, 200, \
            {'Access-Control-Allow-Origin': '*',
             'Access-Control-Allow-Methods': 'GET',
             "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
             }
