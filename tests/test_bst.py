# Define a simple Patient class
class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.id = patient_id
        self.name = name
        self.age = age
        self.condition = condition

    def __str__(self):
        return f"Patient ID: {self.id}, Name: {self.name}, Age: {self.age}, Condition: {self.condition}"


# --- Your BSTNode and PatientBST classes (with corrected __init__ method names) ---
class BSTNode:
    def __init__(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, patient):
        self.root = self._insert_recursive(self.root, patient)

    def _insert_recursive(self, node, patient):
        if not node:
            return BSTNode(patient)
        if patient.id < node.patient.id:
            node.left = self._insert_recursive(node.left, patient)
        else:
            node.right = self._insert_recursive(node.right, patient)
        return node

    def search(self, patient_id):
        return self._search_recursive(self.root, patient_id)

    def _search_recursive(self, node, patient_id):
        if not node:
            return None
        if node.patient.id == patient_id:
            return node.patient
        elif patient_id < node.patient.id:
            return self._search_recursive(node.left, patient_id)
        else:
            return self._search_recursive(node.right, patient_id)

    def delete(self, patient_id):
        self.root, deleted = self._delete_recursive(self.root, patient_id)
        return deleted

    def _delete_recursive(self, node, patient_id):
        if not node:
            return node, None
        if patient_id < node.patient.id:
            node.left, deleted = self._delete_recursive(node.left, patient_id)
        elif patient_id > node.patient.id:
            node.right, deleted = self._delete_recursive(node.right, patient_id)
        else:
            deleted = node.patient
            if not node.left:
                return node.right, deleted
            elif not node.right:
                return node.left, deleted
            min_larger_node = self._min_value_node(node.right)
            node.patient = min_larger_node.patient
            node.right, _ = self._delete_recursive(node.right, min_larger_node.patient.id)
        return node, deleted

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# --- TESTING ---

# Create a new BST
bst = PatientBST()

# Insert some patients
patients = [
    Patient(3, "Alice", 30, "Flu"),
    Patient(1, "Bob", 25, "Cold"),
    Patient(4, "Charlie", 40, "Asthma"),
    Patient(2, "David", 50, "Diabetes"),
]

for p in patients:
    bst.insert(p)

print("✅ Patients inserted.\n")

# Search for a patient
search_id = 2
found = bst.search(search_id)
if found:
    print(f"🔍 Patient Found: {found}\n")
else:
    print(f"❌ Patient with ID {search_id} not found.\n")

# Delete a patient
delete_id = 3
deleted = bst.delete(delete_id)
if deleted:
    print(f"🗑️ Deleted Patient with ID {delete_id}.\n")
else:
    print(f"❌ Patient with ID {delete_id} not found for deletion.\n")

# Try searching for deleted patient
check = bst.search(delete_id)
if check:
    print(f"❗ Patient with ID {delete_id} still exists: {check}\n")
else:
    print(f"✅ Patient with ID {delete_id} is confirmed deleted.\n")
