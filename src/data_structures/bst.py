

class PatientNode:
    def __init__(self, id, name, age, illness):
        self.id = id
        self.name = name
        self.age = age
        self.illness = illness
        self.left = None
        self.right = None

class PatientBST:
    def __init__(self):
        self.root = None

    def insert(self, id, name, age, illness):
        def _insert(node, id, name, age, illness):
            if node is None:
                return PatientNode(id, name, age, illness)
            if id < node.id:
                node.left = _insert(node.left, id, name, age, illness)
            elif id > node.id:
                node.right = _insert(node.right, id, name, age, illness)
            return node
        self.root = _insert(self.root, id, name, age, illness)

    def search(self, id):
        def _search(node, id):
            if node is None or node.id == id:
                return node
            if id < node.id:
                return _search(node.left, id)
            return _search(node.right, id)
        return _search(self.root, id)

    def delete(self, id):
        def _min_value_node(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, id):
            if node is None:
                return None
            if id < node.id:
                node.left = _delete(node.left, id)
            elif id > node.id:
                node.right = _delete(node.right, id)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = _min_value_node(node.right)
                node.id = temp.id
                node.name = temp.name
                node.age = temp.age
                node.illness = temp.illness
                node.right = _delete(node.right, temp.id)
            return node
        self.root = _delete(self.root, id)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append({
                    'id': node.id,
                    'name': node.name,
                    'age': node.age,
                    'illness': node.illness
                })
                _inorder(node.right)
        _inorder(self.root)
        return result
