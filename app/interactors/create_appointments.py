from ..entities import Appointment
from datetime import timedelta

class CreateAppointments:

    def __init__(self,
                 date_time,
                 cost,
                 practitioner,
                 patient,
                 every_number_of_weeks=1,
                 repeat_until=None):
        
        self.date_time = date_time
        self.cost = cost
        self.practitioner = practitioner
        self.patient = patient
        self.every_number_of_weeks = every_number_of_weeks
        self.repeat_until=repeat_until if repeat_until is not None else date_time

    def execute(self):
        for date in self.__date_times_for_appointments():
            Appointment(date_time = date, 
                        cost=self.cost, 
                        practitioner=self.practitioner, 
                        patient_id=self.patient).save()

    def __date_times_for_appointments(self):
            appointments_dates = []
            date = self.date_time
            while date <= self.repeat_until:
                appointments_dates.append(date)
                date += timedelta(days=7)*self.every_number_of_weeks
            return appointments_dates