# tests/test_hospital.py

import unittest
from src.data_structures.linked_list.linkedlist import HospitalLinkedList


class TestHospitalLinkedList(unittest.TestCase):
    def setUp(self):
        self.hospital = HospitalLinkedList()
        self.hospital.add_patient("P001", "Alice", 30, "Flu")
        self.hospital.add_patient("P002", "Bob", 45, "Malaria")

    def test_add_patient(self):
        self.hospital.add_patient("P003", "Charlie", 50, "Injury")
        patients = self.hospital.get_all_patients()
        self.assertEqual(len(patients), 3)
        self.assertEqual(patients[2]['name'], "Charlie")

    def test_get_all_patients(self):
        patients = self.hospital.get_all_patients()
        self.assertEqual(len(patients), 2)
        self.assertEqual(patients[0]['id'], "P001")

    def test_update_patient(self):
        updated = self.hospital.update_patient("P002", name="Bobby", illness="Cold")
        self.assertTrue(updated)
        patients = self.hospital.get_all_patients()
        self.assertEqual(patients[1]['name'], "Bobby")

    def test_delete_patient(self):
        deleted = self.hospital.delete_patient("P001")
        self.assertTrue(deleted)
        patients = self.hospital.get_all_patients()
        self.assertEqual(len(patients), 1)
        self.assertEqual(patients[0]['id'], "P002")

    def test_delete_nonexistent(self):
        deleted = self.hospital.delete_patient("P999")
        self.assertFalse(deleted)

if __name__ == '__main__':
    unittest.main()
