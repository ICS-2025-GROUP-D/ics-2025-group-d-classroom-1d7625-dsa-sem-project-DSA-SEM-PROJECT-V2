


from src.data_structures.bst import PatientBST

def test_insert_and_search():
    bst = PatientBST()
    bst.insert(101, "Alice", 30, "Flu")
    bst.insert(99, "Bob", 40, "Cough")
    bst.insert(110, "Cathy", 25, "Fever")

    result1 = bst.search(101)
    result2 = bst.search(99)
    result3 = bst.search(200)


    print("Search result for ID 101:", result1.name if result1 else "Not found")
    print("Search result for ID 99:", result2.illness if result2 else "Not found")
    print("Search result for ID 200:", result3 if result3 else "Not found")


    assert result1.name == "Alice"
    assert result2.illness == "Cough"
    assert result3 is None

def test_delete():
    bst = PatientBST()
    bst.insert(101, "Alice", 30, "Flu")
    bst.insert(99, "Bob", 40, "Cough")

    bst.delete(101)
    result = bst.search(101)


    print("After deleting 101, search gives:", result if result else "Not found")

    assert result is None
