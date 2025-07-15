class PatientNode:
    def __init__(self, patient_id, name, age, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.illness = illness
        self.next = None

class HospitalLinkedList:
    def __init__(self):
        self.head = None

    def add_patient(self, patient_id, name, age, illness):
        new_node = PatientNode(patient_id, name, age, illness)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_all_patients(self):
        patients = []
        current = self.head
        while current:
            patients.append({
                "id": current.patient_id,
                "name": current.name,
                "age": current.age,
                "illness": current.illness
            })
            current = current.next
        return patients

    def update_patient(self, patient_id, name=None, age=None, illness=None):
        current = self.head
        while current:
            if current.patient_id == patient_id:
                if name:
                    current.name = name
                if age:
                    current.age = age
                if illness:
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
