import pytest
from patient_hashtable import Patient, PatientHashTable

@pytest.fixture
def hashtable():
    return PatientHashTable()

def test_insert_and_get_patient(hashtable):
    patient = Patient(1, 'Alice', 25, 'Flu')
    hashtable.insert_patient(patient)
    result = hashtable.get_patient_by_id(1)
    assert result is not None
    assert result.name == 'Alice'
    assert result.age == 25
    assert result.condition == 'Flu'

def test_get_nonexistent_patient(hashtable):
    assert hashtable.get_patient_by_id(999) is None

def test_delete_patient(hashtable):
    patient = Patient(2, 'Bob', 40, 'Cough')
    hashtable.insert_patient(patient)
    hashtable.delete_patient_by_id(2)
    assert hashtable.get_patient_by_id(2) is None

def test_overwrite_existing_patient(hashtable):
    patient1 = Patient(3, 'Charlie', 50, 'Fever')
    patient2 = Patient(3, 'Charlie B.', 51, 'Recovered')
    hashtable.insert_patient(patient1)
    hashtable.insert_patient(patient2)  # Will not overwrite, warning will print
    result = hashtable.get_patient_by_id(3)
    assert result.name == 'Charlie'  # Should still be the first one inserted
