from collections import deque

class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)

    def peek_order(self):
        return self.queue[0] if self.queue else None

    def process_order(self):
        return self.queue.popleft() if self.queue else None
