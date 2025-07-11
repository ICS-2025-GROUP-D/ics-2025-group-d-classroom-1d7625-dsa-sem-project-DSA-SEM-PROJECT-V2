class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        return f"Patient ID: {self.id}, Name: {self.name}, Age: {self.age}, Condition: {self.condition}"


class PatientHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of buckets

    def _hash(self, patient_id):
        return patient_id % self.size

    def insert_patient(self, patient):
        index = self._hash(patient.id)
        for p in self.table[index]:
            if p.id == patient.id:
                print(f"Patient with ID {patient.id} already exists.")
                return
        self.table[index].append(patient)
        print(f"Inserted: {patient}")

    def get_patient_by_id(self, patient_id):
        index = self._hash(patient_id)
        for p in self.table[index]:
            if p.id == patient_id:
                return p
        return None

    def get_patients_by_name(self, name):
        results = []
        name_lower = name.lower()
        for bucket in self.table:
            for p in bucket:
                if name_lower in p.name.lower():  # Partial and case-insensitive match
                    results.append(p)
        return results

    def delete_patient_by_id(self, patient_id):
        index = self._hash(patient_id)
        for i, p in enumerate(self.table[index]):
            if p.id == patient_id:
                del self.table[index][i]
                print(f"Deleted patient with ID {patient_id}")
                return True
        print(f"Patient with ID {patient_id} not found.")
        return False

    def delete_patients_by_name(self, name):
        name_lower = name.lower()
        deleted_any = False

        for bucket in self.table:
            i = 0
            while i < len(bucket):
                if name_lower in bucket[i].name.lower():  # Match partial name
                    print(f"Deleted: {bucket[i]}")
                    del bucket[i]
                    deleted_any = True
                else:
                    i += 1

        if not deleted_any:
            print(f"No patients found with name containing '{name}'.")

    def display_all_patients(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}:")
                for p in bucket:
                    print(f"  → {p}")

# Time Complexities:
# - insert_patient: O(1) average, O(n) worst (in case of hash collisions)
# - get_patient_by_id: O(1) average, O(n) worst
# - get_patients_by_name: O(n)
# - delete_patient_by_id: O(1) average, O(n) worst
# - delete_patients_by_name: O(n)
# - display_all_patients: O(n)
