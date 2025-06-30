import heapq

class EmergencyHeap:
    def __init__(self):
        self.heap = []

    def admit_patient(self, patient):
        heapq.heappush(self.heap, (patient.urgency, patient))

    def treat_next(self):
        if self.heap:
            return heapq.heappop(self.heap)[1] 
        else:
            return None

    def peek_next(self):
        if self.heap:
            return self.heap[0][1] 
        else:
            return None

    def is_empty(self):
        return len(self.heap) == 0


