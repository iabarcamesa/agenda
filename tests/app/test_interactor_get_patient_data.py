from app.interactors.create_or_update_patient import CreateOrUpdatePatient
from app.interactors.get_patient_data import GetPatientData
from app.entities import Patient
from app.entities.persistence import Persistence as p

def test_create_new_patient():

    p.flush()

    c = CreateOrUpdatePatient(identification='16212513-3', 
                  name='Ignacio Andrés', 
                  first_surname='Abarca', 
                  second_surname='Mesa', 
                  address='Las Araucarias Sur 8563', 
                  state='REGIÓN METROPOLITANA DE SANTIAGO', 
                  county='LA FLORIDA')
    c.execute()

    result = GetPatientData('16212513-3').execute()

    assert result == {
        'identification': '16212513-3', 
        'name': 'Ignacio Andrés', 
        'first_surname': 'Abarca', 
        'second_surname': 'Mesa', 
        'address': 'Las Araucarias Sur 8563', 
        'state': 'REGIÓN METROPOLITANA DE SANTIAGO', 
        'county': 'LA FLORIDA'
    }
