class LinkedListNode:
    def __init__(self, patient):
        self.patient = patient
        self.next = None

class HospitalLinkedList:
    def __init__(self):
        self.head = None

    def append(self, patient):
        new_node = LinkedListNode(patient)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, patient_id):
        current = self.head
        prev = None
        while current:
            if current.patient.id == patient_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
