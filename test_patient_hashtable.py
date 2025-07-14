import unittest
from models.patient import Patient
from data_structures.hash_table import PatientHashTable

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = PatientHashTable()
        self.p1 = Patient(1, "Alice", 30, "Flu", 2)

    def test_insert_and_get(self):
        self.ht.insert(self.p1)
        self.assertEqual(self.ht.get(1).name, "Alice")

    def test_delete(self):
        self.ht.insert(self.p1)
        self.ht.delete(1)
        self.assertIsNone(self.ht.get(1))

if __name__ == '_main_':
    unittest.main()