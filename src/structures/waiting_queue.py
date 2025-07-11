# waiting_queue.py  –– replace ONLY this class block
from collections import deque

class WaitingQueue:
    def __init__(self):
        self.queue = deque()

    # CREATE
    def enqueue(self, patient):
        """Add a patient to the back of the queue."""
        self.queue.append(patient)

    # DELETE
    def dequeue(self):
        """Remove and return the next patient (None if empty)."""
        return self.queue.popleft() if self.queue else None

    # READ (peek)
    def peek(self):
        """Return the next patient without removing (None if empty)."""
        return self.queue[0] if self.queue else None

    # READ (is empty?)
    def is_empty(self):
        return len(self.queue) == 0

    # READ (len(queue))
    def __len__(self):
        return len(self.queue)
