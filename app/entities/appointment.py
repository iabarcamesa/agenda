from .entity import Entity
from .patient import Patient

class Appointment(Entity):

    def __init__(self, date_time, cost, practitioner, patient_id):
        self.date_time = date_time
        self.cost = cost
        self.practitioner = practitioner
        self._patient_id = patient_id

    @property
    def patient(self):
        return self.__load_or_create_patient(self._patient_id)

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
        return cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                              a.date_time.month == month )

    @classmethod
    def find_by_month_and_year_and_practitioner(cls, month, year, practitioner):
        return cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                              a.date_time.month == month and \
                                              a.practitioner == practitioner)

    @classmethod
    def find_by_month_and_year_and_patient(cls, month, year, patient):
        return cls._p.find(cls, key=lambda a: a.date_time.year == year and \
                                              a.date_time.month == month and \
                                              a.patient == patient)


    