from ..entities import Patient

class CreateOrUpdatePatient:

    def __init__(self, identification, name='', first_surname='', second_surname='', address='', state='', county=''):
        self.identification = identification
        self.name = name
        self.first_surname = first_surname 
        self.second_surname = second_surname 
        self.address = address 
        self.state = state
        self.county = county

    def execute(self):
        patient = Patient.find_by_identification(self.identification)

        if patient:
            patient = patient[0]
        else:
            patient = Patient(self.identification)

        patient.name = self.name
        patient.first_surname = self.first_surname 
        patient.second_surname = self.second_surname 
        patient.address = self.address 
        patient.state = self.state
        patient.county = self.county

        patient.save()
