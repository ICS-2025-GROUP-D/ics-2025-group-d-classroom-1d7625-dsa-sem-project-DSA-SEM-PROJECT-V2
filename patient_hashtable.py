class Patient:
    def __init__(self, patient_id, name, age, illness):
        self.id = patient_id
        self.name = name
        self.age = age
        self.illness = illness

class PatientHashTable:
    def __init__(self):
        self.size = 100
        self.table = [[] for _ in range(self.size)]  # Chaining: list of lists

    def _hash(self, key):
        return key % self.size

    def insert(self, patient):
        index = self._hash(patient.id)
        # Check if patient already exists to update
        for i, p in enumerate(self.table[index]):
            if p.id == patient.id:
                self.table[index][i] = patient
                return
        self.table[index].append(patient)

    def search(self, patient_id):
        index = self._hash(patient_id)
        for patient in self.table[index]:
            if patient.id == patient_id:
                return patient
        return None

    def delete(self, patient_id):
        index = self._hash(patient_id)
        for i, patient in enumerate(self.table[index]):
            if patient.id == patient_id:
                del self.table[index][i]
                return True
        return False
