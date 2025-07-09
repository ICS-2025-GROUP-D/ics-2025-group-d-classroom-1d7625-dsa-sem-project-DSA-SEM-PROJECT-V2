from src.data_structures.heap import EmergencyHeap
from src.data_structures.patient import Patient

def test_admit_patient():
    heap = EmergencyHeap()
    p1 = Patient("Alice", "Fever", 3)
    p2 = Patient("Bob", "Stroke", 1)

    heap.admit_patient(p1)
    heap.admit_patient(p2)

    print("Heap after admitting two patients:", heap.heap)
    assert heap.peek_next() == p2

def test_treat_next():
    heap = EmergencyHeap()
    p1 = Patient("Charlie", "Headache", 5)
    p2 = Patient("Diana", "Fracture", 2)

    heap.admit_patient(p1)
    heap.admit_patient(p2)

    treated = heap.treat_next()
    print("Treated patient:", treated)
    assert treated == p2



