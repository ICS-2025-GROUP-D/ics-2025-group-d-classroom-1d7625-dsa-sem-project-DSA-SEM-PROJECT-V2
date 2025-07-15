import heapq

class LowStockMinHeap:
    def __init__(self):
        self.heap = []

    def add_product(self, product):  # ✅ This is the missing method
        quantity = product.get('quantity', 0)
        heapq.heappush(self.heap, (quantity, product))

    def get_lowest_stock(self):
        return [item[1] for item in sorted(self.heap)]
