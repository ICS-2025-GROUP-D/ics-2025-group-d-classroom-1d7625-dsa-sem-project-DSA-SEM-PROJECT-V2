class PatientNode:
    def __init__(self, patient_id, name, age, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.illness = illness
        self.visits = []
        self.next = None

    def __str__(self):
        return f"{self.patient_id}: {self.name}, Age: {self.age}, Illness: {self.illness}"


class HospitalLinkedList:
    def __init__(self):
        self.head = None

    def add_patient(self, patient_id, name, age, illness):
        if self.find_by_id(patient_id):
            raise ValueError(f"Patient ID '{patient_id}' already exists.")
        new_node = PatientNode(patient_id, name, age, illness)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_visit(self, patient_id, visit_note):
        patient = self.find_by_id(patient_id)
        if patient:
            patient.visits.append(visit_note)
            return True
        return False

    def get_visit_history(self, patient_id):
        patient = self.find_by_id(patient_id)
        if patient:
            return patient.visits
        return None

    def get_all_patients(self):
        patients = []
        current = self.head
        while current:
            patients.append({
                "id": current.patient_id,
                "name": current.name,
                "age": current.age,
                "illness": current.illness,
                "visits": current.visits
            })
            current = current.next
        return patients

    def update_patient(self, patient_id, name=None, age=None, illness=None):
        current = self.head
        while current:
            if current.patient_id == patient_id:
                if name is not None:
                    current.name = name
                if age is not None:
                    current.age = age
                if illness is not None:
                    current.illness = illness
                return True
            current = current.next
        return False

    def delete_patient(self, patient_id):
        current = self.head
        prev = None
        while current:
            if current.patient_id == patient_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def find_by_id(self, patient_id):
        current = self.head
        while current:
            if current.patient_id == patient_id:
                return current
            current = current.next
        return None

    def search_patient(self, name=None, illness=None, patient_id=None, age=None):
        results = []
        current = self.head
        while current:
            match = True
            if name and name.lower() not in current.name.lower():
                match = False
            if illness and current.illness != illness:
                match = False
            if patient_id and current.patient_id != patient_id:
                match = False
            if age is not None and current.age != age:
                match = False
            if match:
                results.append({
                    "id": current.patient_id,
                    "name": current.name,
                    "age": current.age,
                    "illness": current.illness,
                    "visits": current.visits
                })
            current = current.next
        return results