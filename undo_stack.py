class Stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size=max_size

    def push(self, item):
        if len(self.stack)>=self.max_size:
            print("Stack is Full!!Cannot Add more patients")
        else:
            self.stack.append(item)
            print(f"Pushed {item}:")

    def pop(self):
        if self.is_empty():
            return "The stack has nothing(empty)"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("\nCurrent Patient in Stack")
            for patient in reversed(self.stack):
                print(f"{patient}")

