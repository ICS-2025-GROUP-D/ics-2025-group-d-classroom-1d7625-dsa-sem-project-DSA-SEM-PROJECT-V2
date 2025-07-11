class PatientHashTable:
    def __init__(self):
        self.table = {}

    def insert(self, patient):
        self.table[patient['id']] = patient

    def get(self, pid):
        return self.table.get(pid)

    def delete(self, pid):
        if pid in self.table:
            del self.table[pid]

# Time Complexities:
# - insert: O(1) average, O(n) worst (in case of hash collisions)
# - get: O(1) average, O(n) worst
# - delete: O(1) average, O(n) worst
