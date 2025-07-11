from src.data_structures.bst import PatientBST

def test_insert_and_search():
    bst = PatientBST()

    patient1 = {'id': 101, 'name': 'Alice', 'age': 30, 'illness': 'Flu'}
    patient2 = {'id': 99, 'name': 'Bob', 'age': 40, 'illness': 'Cough'}
    patient3 = {'id': 110, 'name': 'Cathy', 'age': 25, 'illness': 'Fever'}

    bst.insert(patient1)
    bst.insert(patient2)
    bst.insert(patient3)

    assert bst.search(101)['name'] == 'Alice'
    assert bst.search(99)['illness'] == 'Cough'
    assert bst.search(200) is None

def test_duplicate_insert():
    bst = PatientBST()

    patient = {'id': 101, 'name': 'Alice', 'age': 30, 'illness': 'Flu'}
    bst.insert(patient)
    bst.insert(patient)  # Try inserting again

    result = bst.search(101)
    assert result is not None
    assert result['name'] == 'Alice'
