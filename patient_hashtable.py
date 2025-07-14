class PatientHashTable:
    def _init_(self):
        self.table = {}

    def insert(self, patient):
        self.table[patient.id] = patient

    def delete(self, patient_id):
        if patient_id in self.table:
            del self.table[patient_id]

    def get(self, patient_id):
        return self.table.get(patient_id)