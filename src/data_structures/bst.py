class BSTNode:
    def _init_(self, patient):
        self.patient = patient
        self.left = None
        self.right = None

class PatientBST:
    def _init_(self):
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

    def delete(self, pid):
        def _delete(node, pid):
            if not node:
                return None
            if pid < node.patient['id']:
                node.left = _delete(node.left, pid)
            elif pid > node.patient['id']:
                node.right = _delete(node.right, pid)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_larger_node = _find_min(node.right)
                    node.patient = min_larger_node.patient
                    node.right = _delete(node.right, min_larger_node.patient['id'])
            return node

        def _find_min(node):
            while node.left:
                node = node.left
            return node

        self.root = _delete(self.root, pid)