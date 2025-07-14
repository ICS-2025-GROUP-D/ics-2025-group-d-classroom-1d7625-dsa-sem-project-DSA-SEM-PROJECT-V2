class Patient:
    def __init__(self,id, name, age, illness):
        self.id = id
        self.name = name
        self.age = age
        self.illness = illness

class PatientHashTable:
    def __init__(self):
        self.table = {}

    def insert(self, patient):
        self.table[patient.id] = patient

    def delete(self, patient_id):
        if patient_id in self.table:
            del self.table[patient_id]

    def get(self, patient_id):
        return self.table.get(patient_id)