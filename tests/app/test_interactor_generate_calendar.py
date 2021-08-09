from app.interactors.create_appointments import CreateAppointments
from app.interactors.generate_calendar import GenerateCalendar
from app.entities.persistence import Persistence as p
from datetime import datetime


def test_generate_calendar_grid():
    p.flush()

    expected_calendar_grid = {
        0: {
         'MON': {'day': 26, 'appointments': []},
         'TUE': {'day': 27, 'appointments': []},
         'WED': {'day': 28, 'appointments': []},
         'THU': {'day': 29, 'appointments': []},
         'FRI': {'day': 30, 'appointments': []},
         'SAT': {'day': 31, 'appointments': []},
         'SUN': {'day': 1, 'appointments': []}
        },
        1: {
         'MON': {'day': 2, 'appointments': []},
         'TUE': {'day': 3, 'appointments': []},
         'WED': {'day': 4, 'appointments': []},
         'THU': {'day': 5, 'appointments': []},
         'FRI': {'day': 6, 'appointments': []},
         'SAT': {'day': 7, 'appointments': []},
         'SUN': {'day': 8, 'appointments': []}
        },
        2: {
         'MON': {'day': 9, 'appointments': []},
         'TUE': {'day': 10, 'appointments': []},
         'WED': {'day': 11, 'appointments': []},
         'THU': {'day': 12, 'appointments': []},
         'FRI': {'day': 13, 'appointments': []},
         'SAT': {'day': 14, 'appointments': []},
         'SUN': {'day': 15, 'appointments': []}
        },
        3: {
         'MON': {'day': 16, 'appointments': []},
         'TUE': {'day': 17, 'appointments': []},
         'WED': {'day': 18, 'appointments': []},
         'THU': {'day': 19, 'appointments': []},
         'FRI': {'day': 20, 'appointments': []},
         'SAT': {'day': 21, 'appointments': []},
         'SUN': {'day': 22, 'appointments': []}
        },
        4: {
         'MON': {'day': 23, 'appointments': []},
         'TUE': {'day': 24, 'appointments': []},
         'WED': {'day': 25, 'appointments': []},
         'THU': {'day': 26, 'appointments': []},
         'FRI': {'day': 27, 'appointments': []},
         'SAT': {'day': 28, 'appointments': []},
         'SUN': {'day': 29, 'appointments': []}
        },
        5: {
         'MON': {'day': 30, 'appointments': []},
         'TUE': {'day': 1, 'appointments': []},
         'WED': {'day': 2, 'appointments': []},
         'THU': {'day': 3, 'appointments': []},
         'FRI': {'day': 4, 'appointments': []},
         'SAT': {'day': 5, 'appointments': []},
         'SUN': {'day': 6, 'appointments': []}
        }
    }

    c = GenerateCalendar(month=11, year=2020, practitioner='practitioner_1')
    result = c._GenerateCalendar__calendar_grid()

    assert result == expected_calendar_grid


def test_generate_calendar():
    p.flush()

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

    expected_calendar = {
        0: {
         'MON': {'day': 26, 'appointments': []},
         'TUE': {'day': 27, 'appointments': []},
         'WED': {'day': 28, 'appointments': []},
         'THU': {'day': 29, 'appointments': []},
         'FRI': {'day': 30, 'appointments': []},
         'SAT': {'day': 31, 'appointments': []},
         'SUN': {'day': 1, 'appointments': []}
        },
        1: {
         'MON': {'day': 2, 'appointments': []},
         'TUE': {'day': 3, 'appointments': ['patient_1']},
         'WED': {'day': 4, 'appointments': ['patient_2']},
         'THU': {'day': 5, 'appointments': []},
         'FRI': {'day': 6, 'appointments': []},
         'SAT': {'day': 7, 'appointments': []},
         'SUN': {'day': 8, 'appointments': []}
        },
        2: {
         'MON': {'day': 9, 'appointments': []},
         'TUE': {'day': 10, 'appointments': []},
         'WED': {'day': 11, 'appointments': ['patient_2']},
         'THU': {'day': 12, 'appointments': []},
         'FRI': {'day': 13, 'appointments': []},
         'SAT': {'day': 14, 'appointments': []},
         'SUN': {'day': 15, 'appointments': []}
        },
        3: {
         'MON': {'day': 16, 'appointments': []},
         'TUE': {'day': 17, 'appointments': ['patient_1']},
         'WED': {'day': 18, 'appointments': ['patient_2']},
         'THU': {'day': 19, 'appointments': []},
         'FRI': {'day': 20, 'appointments': []},
         'SAT': {'day': 21, 'appointments': []},
         'SUN': {'day': 22, 'appointments': []}
        },
        4: {
         'MON': {'day': 23, 'appointments': []},
         'TUE': {'day': 24, 'appointments': []},
         'WED': {'day': 25, 'appointments': ['patient_2']},
         'THU': {'day': 26, 'appointments': []},
         'FRI': {'day': 27, 'appointments': []},
         'SAT': {'day': 28, 'appointments': []},
         'SUN': {'day': 29, 'appointments': []}
        },
        5: {
         'MON': {'day': 30, 'appointments': []},
         'TUE': {'day': 1, 'appointments': []},
         'WED': {'day': 2, 'appointments': []},
         'THU': {'day': 3, 'appointments': []},
         'FRI': {'day': 4, 'appointments': []},
         'SAT': {'day': 5, 'appointments': []},
         'SUN': {'day': 6, 'appointments': []}
        }
    }

    c = GenerateCalendar(month=11, year=2020, practitioner='practitioner_1')
    result = c.execute()

    assert result == expected_calendar