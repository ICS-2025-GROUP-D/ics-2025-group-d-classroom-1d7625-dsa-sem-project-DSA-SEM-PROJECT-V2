class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"[Insert] {data} added as head node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"[Insert] {data} appended to the list.")

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"[Delete] {data} removed from the list.")
                return True
            prev = current
            current = current.next
        print(f"[Delete] {data} not found.")
        return False

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(f"[Search] {data} found in the list.")
                return True
            current = current.next
        print(f"[Search] {data} not found.")
        return False

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f"[Update] {old_data} changed to {new_data}.")
                return True
            current = current.next
        print(f"[Update] {old_data} not found.")
        return False

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(f"[To List] Current list: {elements}")
        return elements
