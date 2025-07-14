import pytest
from patient_hashtable import Patient, PatientHashTable

@pytest.fixture
def hashtable():
    return PatientHashTable()

def test_insert_and_get_patient(hashtable):
    patient = Patient(1, 'Ocean', 25, 'Flu')
    hashtable.insert(patient)
    result = hashtable.get(1)
    assert result is not None
    assert result.name == 'Ocean'
    assert result.age == 25
    assert result.illness == 'Flu'

def test_get_nonexistent_patient(hashtable):
    assert hashtable.get(999) is None

def test_delete_patient(hashtable):
    patient = Patient(2, 'Leo', 40, 'Cough')
    hashtable.insert(patient)
    hashtable.delete(2)
    assert hashtable.get(2) is None

def test_overwrite_existing_patient(hashtable):
    patient1 = Patient(3, 'Charlie', 50, 'Fever')
    patient2 = Patient(3, 'Charlie B.', 51, 'Recovered')
    hashtable.insert(patient1)
    hashtable.insert(patient2)
    result = hashtable.get(3)
    assert result.name == 'Charlie B.'
    assert result.age == 51
    assert result.illness == 'Recovered'
