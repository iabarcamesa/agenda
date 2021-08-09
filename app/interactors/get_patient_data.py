from app.entities import Patient

class GetPatientData:

    def __init__(self, identification):
        self.identification = identification

    def execute(self):
        patient = Patient.find_by_identification(self.identification)
        if not patient:
            patient = {}
        else:
            patient = {
                'identification': patient[0].identification, 
                'name': patient[0].name,
                'first_surname': patient[0].first_surname, 
                'second_surname': patient[0].second_surname, 
                'address': patient[0].address, 
                'state': patient[0].state,
                'county': patient[0].county
            }
        return patient
