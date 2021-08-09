from app.interactors.create_appointments import CreateAppointments
from app.entities import Appointment
from app.entities.persistence import Persistence as p
from datetime import datetime

def test_create_unique_appointment():
    p.flush()

    c = CreateAppointments(date_time=datetime(2020,11,26),
                          cost=100,
                          practitioner='practitioner_1',
                          patient='patient_1')
    c.execute()

    result = Appointment.find_by_month_and_year(year=2020, month=11)

    assert len(result) == 1
    assert set([datetime(2020,11,26)]) == \
           set([a.date_time for a in result])

def test_create_appointment_every_week():
    p.flush()

    c = CreateAppointments(date_time=datetime(2020,11,3),
                          cost=100,
                          practitioner='practitioner_1',
                          patient='patient_1',
                          every_number_of_weeks=1,
                          repeat_until=datetime(2020,11,26))

    c.execute()

    result = Appointment.find_by_month_and_year(year=2020, month=11)

    assert len(result) == 4
    assert set([datetime(2020,11,3), datetime(2020,11,10), datetime(2020,11,17), datetime(2020,11,24)]) == \
           set([a.date_time for a in result])

def test_create_appoimtment_every_two_weeks():
    p.flush()

    c = CreateAppointments(date_time=datetime(2020,11,3),
                          cost=100,
                          practitioner='practitioner_1',
                          patient='patient_1',
                          every_number_of_weeks=2,
                          repeat_until=datetime(2020,11,26))

    c.execute()

    result = Appointment.find_by_month_and_year(year=2020, month=11)

    assert len(result) == 2
    assert set([datetime(2020,11,3), datetime(2020,11,17)]) == \
           set([a.date_time for a in result])