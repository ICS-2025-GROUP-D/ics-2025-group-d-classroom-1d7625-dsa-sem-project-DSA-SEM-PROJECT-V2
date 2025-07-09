from src.data_structures.hash_table import Patient, PatientHashTable

def test_insert_and_get_patient():
    table = PatientHashTable()
    patient = Patient(1, "Alice", 30, "Flu")
    table.insert_patient(patient)
    result = table.get_patient_by_id(1)
    assert result is not None
    assert result.name == "Alice"
    assert result.age == 30
    assert result.condition == "Flu"

def test_duplicate_patient_insert():
    table = PatientHashTable()
    patient1 = Patient(2, "Bob", 40, "Cold")
    patient2 = Patient(2, "Bob", 40, "Cold")
    table.insert_patient(patient1)
    table.insert_patient(patient2)
    bucket = table.table[table._hash(2)]
    assert len(bucket) == 1  # Duplicate should not be added

def test_delete_patient():
    table = PatientHashTable()
    patient = Patient(3, "Charlie", 25, "Fever")
    table.insert_patient(patient)
    deleted = table.delete_patient_by_id(3)
    assert deleted is True
    assert table.get_patient_by_id(3) is None

def test_delete_nonexistent_patient():
    table = PatientHashTable()
    deleted = table.delete_patient_by_id(99)
    assert deleted is False
