

import pytest
from patient_hashtable import PatientHashTable

@pytest.fixture
def hashtable():
    return PatientHashTable()

def test_insert_and_get_patient(hashtable):
    patient = {'id': 'P001', 'name': 'Alice', 'age': 25}
    hashtable.insert(patient)
    assert hashtable.get('P001') == patient

def test_get_nonexistent_patient(hashtable):
    assert hashtable.get('P999') is None

def test_delete_patient(hashtable):
    patient = {'id': 'P002', 'name': 'Bob', 'age': 40}
    hashtable.insert(patient)
    hashtable.delete('P002')
    assert hashtable.get('P002') is None

def test_overwrite_existing_patient(hashtable):
    patient1 = {'id': 'P003', 'name': 'Charlie', 'age': 50}
    patient2 = {'id': 'P003', 'name': 'Charlie B.', 'age': 51}
    hashtable.insert(patient1)
    hashtable.insert(patient2)
    assert hashtable.get('P003') == patient2
