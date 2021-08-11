from app.entities import Appointment
from app.entities import Patient
from app.entities.persistence import Persistence as p
from datetime import datetime

def test_save_appointment():

    p.flush()

    a_1 = Appointment(date_time = datetime(2020,11,22), 
                      cost=100, 
                      practitioner='practitioner_1', 
                      patient=Patient('patient_1'))

    a_1.save()

    result = p.find(Appointment, key=lambda a: a.practitioner=='practitioner_1')

    assert len(result) == 1
    assert result[0].practitioner == 'practitioner_1'

def test_find_appointments_by_month_and_year():

    p.flush()
    Patient(identification='patient_1').save()

    a_1 = Appointment(date_time = datetime(2020,11,22), 
                    cost=100, 
                    practitioner='practitioner_1', 
                    patient=Patient('patient_1')).save()

    a_2 = Appointment(date_time = datetime(2020,11,11), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient('patient_1')).save()


    a_3 = Appointment(date_time = datetime(2020,11,1), 
                    cost=100, 
                    practitioner='practitioner_1', 
                    patient=Patient('patient_1')).save()

    a_4 = Appointment(date_time = datetime(2020,10,26), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient('patient_1')).save()

    result = Appointment.find_by_month_and_year(year=2020, month=11)

    assert len(result) == 3
    assert set([datetime(2020,11,22), datetime(2020,11,11), datetime(2020,11,1)]) == \
           set([a.date_time for a in result])

def test_find_appointments_by_month_and_year_and_practitioner():

    p.flush()
    Patient(identification='patient_1').save()

    a_1 = Appointment(date_time = datetime(2020,11,22), 
                    cost=100, 
                    practitioner='practitioner_1', 
                    patient=Patient('patient_1')).save()

    a_2 = Appointment(date_time = datetime(2020,11,11), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient('patient_1')).save()


    a_3 = Appointment(date_time = datetime(2020,11,1), 
                    cost=100, 
                    practitioner='practitioner_2', 
                    patient=Patient('patient_1')).save()

    a_4 = Appointment(date_time = datetime(2020,10,26), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient('patient_1')).save()

    result = Appointment.find_by_month_and_year_and_practitioner(year=2020, month=11, practitioner='practitioner_1')

    assert len(result) == 2
    assert set([datetime(2020,11,22), datetime(2020,11,11)]) == \
           set([a.date_time for a in result])

def test_find_appointments_by_month_and_year_and_patient():

    p.flush()
    Patient(identification='patient_1').save()

    a_1 = Appointment(date_time = datetime(2020,11,22), 
                    cost=100, 
                    practitioner='practitioner_1', 
                    patient=Patient('patient_1')).save()

    a_2 = Appointment(date_time = datetime(2020,11,11), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient('patient_2')).save()


    a_3 = Appointment(date_time = datetime(2020,11,1), 
                    cost=100, 
                    practitioner='practitioner_1', 
                    patient=Patient('patient_1')).save()

    a_4 = Appointment(date_time = datetime(2020,10,26), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient('patient_1')).save()

    result = Appointment.find_by_month_and_year_and_patient(year=2020, month=11, patient='patient_1')

    assert len(result) == 2
    assert set([datetime(2020,11,22), datetime(2020,11,1)]) == \
           set([a.date_time for a in result])

def test_find_appointments_whith_existing_patient():

    p.flush()

    Patient(identification='16212513-3', 
            name='Ignacio Andrés', 
            first_surname='Abarca', 
            second_surname='Mesa', 
            address='Las Araucarias Sur 8563', 
            state='REGIÓN METROPOLITANA DE SANTIAGO', 
            county='LA FLORIDA').save()

    Appointment(date_time = datetime(2020,11,22), 
                cost=100, 
                practitioner='practitioner_1', 
                patient=Patient.find_by_identification('16212513-3')[0]).save()

    patient = Appointment.find_by_month_and_year(year=2020, month=11)[0].patient

    assert patient.identification == '16212513-3'
    assert patient.name == 'Ignacio Andrés'
    assert patient.first_surname == 'Abarca' 
    assert patient.second_surname == 'Mesa'
    assert patient.address == 'Las Araucarias Sur 8563'
    assert patient.state == 'REGIÓN METROPOLITANA DE SANTIAGO'
    assert patient.county == 'LA FLORIDA'