from flask import Blueprint
from flask import request
from flask_restx import Api, apidoc

from api.namespaces.authenticate import ns as authenticate
from api.namespaces.create_appointment import ns as create_appointment
from api.namespaces.generate_invoice import ns as generate_invoice
from api.namespaces.generate_calendar import ns as generate_calendar
from api.namespaces.patient import ns as patient

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    blueprint,
    doc='/docs',
    version='0.0.2',
    title='',
    description='',
    security='apikey',
    authorizations=authorizations
)


@api.documentation
def custom_ui(*args, **kwargs):
    print(request.headers)
    return apidoc.ui_for(api)

api.add_namespace(authenticate)
api.add_namespace(create_appointment)
api.add_namespace(generate_invoice)
api.add_namespace(generate_calendar)
api.add_namespace(patient)
