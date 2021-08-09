from app.entities import Appointment

class GenerateInvoice:

    def __init__(self, month, year, practitioner):
        self.month = month
        self.year = year
        self.practitioner = practitioner

    @property
    def _appointments(self):
        return Appointment.find_by_month_and_year_and_practitioner(
            self.month, 
            self.year, 
            self.practitioner)

    def execute(self):

        patients_invoices_aux = {}

        for appointment in self._appointments:
            patient_invoice = get_patient_invoice(appointment.patient,
                                                  patients_invoices_aux)
            patient_invoice['total'] += appointment.cost
            patient_invoice['invoices'].append({'date': appointment.date_time,
                                                'text': 'SESION DE FONOAUDIOLOGIA ' + str(appointment.date_time.day).zfill(2) + '/' + str(appointment.date_time.month).zfill(2),
                                                'amount': appointment.cost})

        return to_list(patients_invoices_aux)


def to_list(patients_invoices):
    result = []
    for _, value in patients_invoices.items():
        result.append(value)
    return result


def get_patient_invoice(patient, patients_invoices_aux):
    if not patients_invoices_aux.get(patient):
        patients_invoices_aux[patient] = {'patient': ' '.join([patient.name, patient.first_surname, patient.second_surname]),
                                          'name': ' '.join([patient.name, patient.first_surname, patient.second_surname]),
                                          'address': patient.address,
                                          'state': patient.state, 
                                          'county': patient.county,
                                          'identification': patient.identification,
                                          'total': 0,
                                          'invoices': []
                                        }
    return patients_invoices_aux[patient]