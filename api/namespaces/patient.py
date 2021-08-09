from flask import request
from flask_restx import Namespace, Resource, cors

from app.interactors.create_or_update_patient import CreateOrUpdatePatient
from app.interactors.get_patient_data import GetPatientData

ns = Namespace('patient',
               description='Description')


@ns.route('')
class PatientEndpoint(Resource):

    @cors.crossdomain(origin='*')
    @ns.param('identification', '', type=str, default='12345678-9')
    @ns.param('name', 'Name', type=str, default='Name')
    @ns.param('first_surname', 'First Surname', type=str, default='First Surname')
    @ns.param('second_surname', 'Second Surname', type=str, default='Second Surname')
    @ns.param('address', 'Address', type=str, default='Street Name 123')
    @ns.param('state', 'State', type=str, default='STATE')
    @ns.param('county', 'County', type=str, default='COUNTY')
    def post(self):
        '''Get data'''

        try:
            CreateOrUpdatePatient(
                identification=request.args['identification'], 
                name=request.args['name'], 
                first_surname=request.args['first_surname'], 
                second_surname=request.args['second_surname'], 
                address=request.args['address'], 
                state=request.args['state'], 
                county=request.args['county']
            ).execute()
            return {'data': 'Patient created or updated'}
        except Exception as e:
            return str(e), 400

    @cors.crossdomain(origin='*')
    @ns.param('identification', '', type=str, default='12345678-9')
    def get(self):
        try:
           return GetPatientData(request.args['identification']).execute()
        except Exception as e:
            return str(e), 400


    def options(self):
        return {'Allow': 'GET'}, 200, \
            {'Access-Control-Allow-Origin': '*',
             'Access-Control-Allow-Methods': 'GET',
             "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
             }
