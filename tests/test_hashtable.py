import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '', 'InventoryApp'))
sys.path.insert(0, project_root)


from src.ds.hash_table import ProductHashTable

def test_insert_and_search():
    ht = ProductHashTable()
    ht.add_product("P001", {"name": "Milk", "qty": 3})
    assert ht.get_product("P001")["name"] == "Milk"

def test_delete():
    ht = ProductHashTable()
    ht.add_product("P001", {"name": "Milk"})
    ht.delete_product("P001")
    assert ht.get_product("P001") is None
