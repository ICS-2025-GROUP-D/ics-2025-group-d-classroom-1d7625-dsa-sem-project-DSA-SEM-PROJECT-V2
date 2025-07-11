import heapq

class EmergencyHeap:
    def __init__(self):
        self.heap = []
        self.counter = 0  # To avoid priority tie issues

    def add_emergency(self, patient, priority):
        heapq.heappush(self.heap, (priority, self.counter, patient))
        self.counter += 1

    def get_next(self):
        return heapq.heappop(self.heap)[2] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0


