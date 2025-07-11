class BSTNode:
    def __init__(self, patient):
        self.patient = patient  # A dictionary e.g. {'id': 5, 'name': 'John'}
        self.left = None
        self.right = None

class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, patient):
        def _insert(node, patient):
            if not node:
                return BSTNode(patient)
            if patient['id'] < node.patient['id']:
                node.left = _insert(node.left, patient)
            else:
                node.right = _insert(node.right, patient)
            return node
        self.root = _insert(self.root, patient)

    def search(self, pid):
        def _search(node, pid):
            if not node:
                return None
            if pid == node.patient['id']:
                return node.patient
            elif pid < node.patient['id']:
                return _search(node.left, pid)
            else:
                return _search(node.right, pid)
        return _search(self.root, pid)
