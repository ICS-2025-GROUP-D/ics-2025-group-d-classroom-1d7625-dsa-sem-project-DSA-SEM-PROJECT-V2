class BSTNode:
    def _init_(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class PatientBST:
    def _init_(self):
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
        self.root, _ = self._delete_recursive(self.root, patient_id)

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