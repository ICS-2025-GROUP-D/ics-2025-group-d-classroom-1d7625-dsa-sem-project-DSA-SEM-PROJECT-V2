from src.linked_list import LinkedList


def test_insert():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    assert ll.to_list() == ["A", "B"]

def test_delete():
    ll = LinkedList()
    ll.insert("A")
    ll.insert("B")
    assert ll.delete("A") is True
    assert ll.delete("Z") is False
    assert ll.to_list() == ["B"]

def test_search():
    ll = LinkedList()
    ll.insert("X")
    assert ll.search("X") is True
    assert ll.search("Y") is False

def test_update():
    ll = LinkedList()
    ll.insert("Old")
    assert ll.update("Old", "New") is True
    assert ll.update("Missing", "X") is False
    assert ll.to_list() == ["New"]
