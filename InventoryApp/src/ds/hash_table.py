
class ProductHashTable:
    def __init__(self):
        self.table = {}

    def add_product(self, sku, product):
        self.table[sku] = product

    def get_product(self, sku):
        return self.table.get(sku)

    def delete_product(self, sku):
        if sku in self.table:
            del self.table[sku]
