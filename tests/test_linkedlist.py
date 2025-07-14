import unittest
from src.data_structures.linked_list.patient import Patient
from data_structures.hospital_linkedlist import HospitalLinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = HospitalLinkedList()
        self.p1 = Patient(1, "Alice", 30, "Flu", 2)
        self.p2 = Patient(2, "Bob", 25, "Cold", 1)

    def test_append_and_find(self):
        self.ll.append(self.p1)
        self.ll.append(self.p2)
        self.assertEqual(self.ll.find(1).name, "Alice")
        self.assertEqual(self.ll.find(2).name, "Bob")

    def test_delete(self):
        self.ll.append(self.p1)
        self.ll.delete(1)
        self.assertIsNone(self.ll.find(1))

if _name_ == '_main_':
    unittest.main()