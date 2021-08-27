from copy import deepcopy
from .entity import Entity
from .patient import Patient

class AppointmentFunctional:

    def __init__(self, date_time, cost, practitioner, patient):
        assert isinstance(patient, Patient)
        self.date_time = date_time
        self.cost = cost
        self.practitioner = practitioner
        self.patient = patient

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, value):
        assert isinstance(value, Patient)
        self._patient = value


class AppointmentData(Entity):

    data_class = AppointmentFunctional

    @classmethod
    def set_data_class(cls, data_class):
        cls.data_class = data_class

    @classmethod
    def save(cls, appointment):
        appointment_to_save = deepcopy(appointment)
        appointment_to_save._patient = appointment.patient.identification
        cls._p.save(appointment_to_save)

    @classmethod
    def find_by_month_and_year(cls, month, year):
        read_data =  cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                                    a.date_time.month == month )
        return [
            cls.data_class(
                data.date_time,
                data.cost,
                data.practitioner,
                Patient.find_by_identification(data.patient)[0]
            ) 
        for data in read_data]

    @classmethod
    def find_by_month_and_year_and_practitioner(cls, month, year, practitioner):
        read_data = cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                              a.date_time.month == month and \
                                              a.practitioner == practitioner)
        return [
            cls.data_class(
                data.date_time,
                data.cost,
                data.practitioner,
                Patient.find_by_identification(data.patient)[0]
            ) 
        for data in read_data]

    @classmethod
    def find_by_month_and_year_and_patient(cls, month, year, patient):
        read_data = cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                              a.date_time.month == month and \
                                              a.patient == patient)
        return [
            cls.data_class(
                data.date_time,
                data.cost,
                data.practitioner,
                Patient.find_by_identification(data.patient)[0]
            ) 
        for data in read_data]


class Appointment(AppointmentFunctional, AppointmentData):
    
    def __init__(self, *args, **kwargs):
        self.set_data_class(self.__class__)
        super().__init__(*args, **kwargs)

    def save(self):
        super().save(self)


    