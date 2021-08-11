from .entity import Entity
from .patient import Patient

class AppointmentFunctional:

    def __init__(self, date_time, cost, practitioner, patient):
        self.date_time = date_time
        self.cost = cost
        self.practitioner = practitioner
        self.patient = patient


class AppointmentData(Entity):

    data_class = AppointmentFunctional

    @classmethod
    def set_data_class(cls, data_class):
        cls.data_class = data_class

    def save(self, appointment):
        if isinstance(appointment.patient, Patient):
            appointment.patient = appointment.patient.identification
        self._p.save(appointment)

    @staticmethod
    def __load_or_create_patient(patient_id):
        loaded_patient = Patient.find_by_identification(patient_id)
        if loaded_patient:
            return loaded_patient[0]
        else:
            patient = Patient(patient_id)
            patient.save()
            return patient

    @classmethod
    def find_by_month_and_year(cls, month, year):
        read_data =  cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                                    a.date_time.month == month )
        return [
            cls.data_class(
                data.date_time,
                data.cost,
                data.practitioner,
                cls.__load_or_create_patient(data.patient)
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
                cls.__load_or_create_patient(data.patient)
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
                cls.__load_or_create_patient(data.patient)
            ) 
        for data in read_data]


class Appointment(AppointmentFunctional, AppointmentData):
    
    def __init__(self, *args, **kwargs):
        self.set_data_class(self.__class__)
        super().__init__(*args, **kwargs)

    def save(self):
        super().save(self)


    