from app.interactors.create_appointments import CreateAppointments
from app.interactors.create_or_update_patient import CreateOrUpdatePatient
from app.interactors.generate_invoice import GenerateInvoice
from app.entities.persistence import Persistence as p
from datetime import datetime

def test_save_appointment():
    p.flush()

    CreateOrUpdatePatient(identification='patient_1', 
                  name='Name', 
                  first_surname='Test', 
                  second_surname='One', 
                  address='Street Name 123', 
                  state='REGIÓN METROPOLITANA DE SANTIAGO', 
                  county='LA FLORIDA').execute()

    CreateOrUpdatePatient(identification='patient_2', 
                  name='Name', 
                  first_surname='Test', 
                  second_surname='Two', 
                  address='Street Name 456', 
                  state='REGIÓN METROPOLITANA DE SANTIAGO', 
                  county='LA FLORIDA').execute()

    CreateAppointments(date_time=datetime(2020,11,3),
                       cost=100,
                       practitioner='practitioner_1',
                       patient='patient_1',
                       every_number_of_weeks=2,
                       repeat_until=datetime(2020,11,26)).execute()

    CreateAppointments(date_time=datetime(2020,11,4),
                    cost=80,
                    practitioner='practitioner_1',
                    patient='patient_2',
                    every_number_of_weeks=1,
                    repeat_until=datetime(2020,11,26)).execute()

    expected_invoices = [
        {
        'patient': 'Name Test One',
        'total': 200,
        'name': 'Name Test One',
        'address': 'Street Name 123',
        'state': 'REGIÓN METROPOLITANA DE SANTIAGO', 
        'county': 'LA FLORIDA',
        'identification': 'patient_1',
        'invoices': [{'date': datetime(2020,11,3), 'amount': 100, 'text': 'SESION DE FONOAUDIOLOGIA 03/11'},
                     {'date': datetime(2020,11,17), 'amount': 100, 'text': 'SESION DE FONOAUDIOLOGIA 17/11'}
                    ]
        },
                {
        'patient': 'Name Test Two',
        'total': 320,
        'identification': 'patient_2',
        'name': 'Name Test Two',
        'address': 'Street Name 456',
        'state': 'REGIÓN METROPOLITANA DE SANTIAGO', 
        'county': 'LA FLORIDA',
        'invoices': [{'date': datetime(2020,11,4), 'amount': 80, 'text': 'SESION DE FONOAUDIOLOGIA 04/11'},
                     {'date': datetime(2020,11,11), 'amount': 80, 'text': 'SESION DE FONOAUDIOLOGIA 11/11'}, 
                     {'date': datetime(2020,11,18), 'amount': 80, 'text': 'SESION DE FONOAUDIOLOGIA 18/11'}, 
                     {'date': datetime(2020,11,25), 'amount': 80, 'text': 'SESION DE FONOAUDIOLOGIA 25/11'} 
                    ]
        }
        ]


    c = GenerateInvoice(month=11, year=2020, practitioner='practitioner_1')
    result = c.execute()

    print(result)

    assert sorted(result,key=lambda i: i['patient']) == sorted(expected_invoices,key=lambda i: i['patient'])