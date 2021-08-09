from .entity import Entity

class Patient(Entity):

    def __init__(self, identification, name='', first_surname='', second_surname='', address='', state='', county=''):
        self.identification = identification
        self.name = name
        self.first_surname = first_surname 
        self.second_surname = second_surname 
        self.address = address 
        self.state = state
        self.county = county

    def __str__(self):
        return self.identification

    def __eq__(self, o: object) -> bool:
        o_identification = o if isinstance(o,str) else o.identification
        return self.identification == o_identification

    def __hash__(self) -> int:
        return hash(self.identification)

    @classmethod
    def find_by_identification(cls, identification):
        patient_list = cls._p.find(cls, key=lambda a: a.identification == identification)
        return patient_list
