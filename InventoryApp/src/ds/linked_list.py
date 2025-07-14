class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class RestockLinkedList:
    def __init__(self):
        self.head = None

    def log_restock(self, entry):
        new_node = Node(entry)
        new_node.next = self.head
        self.head = new_node

    def get_all_logs(self):
        logs = []
        current = self.head
        while current:
            logs.append(current.data)
            current = current.next
        return logs  # ✅ This must be here
