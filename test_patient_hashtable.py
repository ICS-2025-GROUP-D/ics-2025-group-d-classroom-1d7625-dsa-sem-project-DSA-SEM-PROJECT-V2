import pytest
from patient_hashtable import Patient, PatientHashTable

@pytest.fixture
def hashtable():
    return PatientHashTable()

def test_insert_and_get_patient(hashtable):
    patient = Patient(1, 'Alice', 25, 'Flu')
    hashtable.insert(patient)
    result = hashtable.search(1)
    assert result is not None
    assert result.name == 'Alice'
    assert result.age == 25
    assert result.illness == 'Flu'

def test_get_nonexistent_patient(hashtable):
    assert hashtable.search(999) is None

def test_delete_patient(hashtable):
    patient = Patient(2, 'Bob', 40, 'Cough')
    hashtable.insert(patient)
    hashtable.delete(2)
    assert hashtable.search(2) is None

def test_overwrite_existing_patient(hashtable):
    patient1 = Patient(3, 'Charlie', 50, 'Fever')
    patient2 = Patient(3, 'Charlie B.', 51, 'Recovered')
    hashtable.insert(patient1)
    hashtable.insert(patient2)  # Overwrites existing patient with same ID
    result = hashtable.search(3)
    assert result.name == 'Charlie B.'
    assert result.age == 51
    assert result.illness == 'Recovered'
