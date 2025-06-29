# tests/test_bst.py

from src.data_structures.bst import PatientBST

def test_insert_and_search():
    bst = PatientBST()
    bst.insert(101, "Alice", 30, "Flu")
    bst.insert(99, "Bob", 40, "Cough")
    bst.insert(110, "Cathy", 25, "Fever")

    assert bst.search(101).name == "Alice"
    assert bst.search(99).illness == "Cough"
    assert bst.search(200) is None

def test_delete():
    bst = PatientBST()
    bst.insert(101, "Alice", 30, "Flu")
    bst.insert(99, "Bob", 40, "Cough")
    bst.delete(101)
    assert bst.search(101) is None
