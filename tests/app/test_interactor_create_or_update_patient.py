from app.interactors.create_or_update_patient import CreateOrUpdatePatient
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

    result = Patient.find_by_identification('16212513-3')

    assert len(result) == 1
    assert result[0].identification == '16212513-3'
    assert result[0].name == 'Ignacio Andrés'
    assert result[0].first_surname == 'Abarca' 
    assert result[0].second_surname == 'Mesa' 
    assert result[0].address == 'Las Araucarias Sur 8563'
    assert result[0].state == 'REGIÓN METROPOLITANA DE SANTIAGO'
    assert result[0].county == 'LA FLORIDA'

def test_update_existing_patient():

    p.flush()

    c_1 = CreateOrUpdatePatient(identification='16212513-3', 
                  name='Ignacio Andrés', 
                  first_surname='Abarca', 
                  second_surname='Mesa', 
                  address='Las Araucarias Sur 8563', 
                  state='REGIÓN METROPOLITANA DE SANTIAGO', 
                  county='LA FLORIDA')
    c_1.execute()

    patient = Patient.find_by_identification('16212513-3')[0]

    assert patient.identification == '16212513-3'
    assert patient.name == 'Ignacio Andrés'
    assert patient.first_surname == 'Abarca' 
    assert patient.second_surname == 'Mesa' 
    assert patient.address == 'Las Araucarias Sur 8563'
    assert patient.state == 'REGIÓN METROPOLITANA DE SANTIAGO'
    assert patient.county == 'LA FLORIDA'

    c_2 = CreateOrUpdatePatient(identification='16212513-3', 
                name='Ignacio Andrés', 
                first_surname='Abarca', 
                second_surname='Mesa', 
                address='Marcela Paz 1893', 
                state='REGIÓN METROPOLITANA DE SANTIAGO', 
                county='LAS CONDES')
    c_2.execute()

    result = Patient.find_by_identification('16212513-3')
    assert len(result) == 1

    patient = result[0]
    assert patient.identification == '16212513-3'
    assert patient.name == 'Ignacio Andrés'
    assert patient.first_surname == 'Abarca' 
    assert patient.second_surname == 'Mesa' 
    assert patient.address == 'Marcela Paz 1893'
    assert patient.state == 'REGIÓN METROPOLITANA DE SANTIAGO'
    assert patient.county == 'LAS CONDES'
