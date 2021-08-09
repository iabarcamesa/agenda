from app.entities import Patient
from app.entities.persistence import Persistence as p
from datetime import datetime

def test_save_appointment():

    p.flush()

    p_1 = Patient(identification='16212513-3', 
                  name='Ignacio Andrés', 
                  first_surname='Abarca', 
                  second_surname='Mesa', 
                  address='Las Araucarias Sur 8563', 
                  state='REGIÓN METROPOLITANA DE SANTIAGO', 
                  county='LA FLORIDA')

    p_1.save()

    result = p.find(Patient, key=lambda p: p.identification=='16212513-3')

    assert len(result) == 1
    assert result[0].identification == '16212513-3'

def test_find_appointments_by_month_and_year():

    p.flush()

    p_1 = Patient(identification='16212513-3', 
                  name='Ignacio Andrés', 
                  first_surname='Abarca', 
                  second_surname='Mesa', 
                  address='Las Araucarias Sur 8563', 
                  state='REGIÓN METROPOLITANA DE SANTIAGO', 
                  county='LA FLORIDA')
    p_1.save()

    result = Patient.find_by_identification(identification='16212513-3')

    assert len(result) == 1
    assert result[0].identification == '16212513-3'
    assert result[0].name == 'Ignacio Andrés'
    assert result[0].first_surname == 'Abarca' 
    assert result[0].second_surname == 'Mesa'
    assert result[0].address == 'Las Araucarias Sur 8563'
    assert result[0].state == 'REGIÓN METROPOLITANA DE SANTIAGO'
    assert result[0].county == 'LA FLORIDA'