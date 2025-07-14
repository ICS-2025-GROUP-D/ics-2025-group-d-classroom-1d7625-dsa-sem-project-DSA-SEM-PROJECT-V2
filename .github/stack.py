class Patient:
    def __init__(self,name,pat_ID,illness):
        self.name=name
        self.pat_ID=pat_ID
        self.illness=illness

    def __repr__(self):
        return f"Patient(name={self.name}, ID={self.pat_ID}, illness={self.illness})"

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
        print(f"Pushed {item}:")

    def pop(self):
        if self.is_empty():
            return "The stack has nothing(empty)"
        return self.stack.pop()


    def is_empty(self):
        return len(self.stack)==0


    def display(self):
        print("Stack:",self.stack)

class Undo:
    def __init__(self):
        self.undo_stack=Stack()

    def add_info(self,info,patient):
        description = f"{info} {patient.name} - {patient.illness}"

        self.undo_stack.push(description)

    def undo_last_info(self):
        if self.undo_stack.is_empty():
            return "Nothing to undo in stack"
        else:
            info=self.undo_stack.pop()
            print(f"Undoing:{info}")

    def show_info(self):
        self.undo_stack.display()

# Create patients
p1 = Patient("Joseph", 10045, "Malaria")
p2 = Patient("Maria", 10047, "Typhoid")

# Create stacks
patient_stack = Stack()
undo_stack = Undo()

# Add patients
patient_stack.push(p1)
undo_stack.add_info("Added", p1)

patient_stack.push(p2)
undo_stack.add_info("Added", p2)

# Pop a patient
removed = patient_stack.pop()
if isinstance(removed, Patient):
    undo_stack.add_info("Deleted", removed)

print("\n-- Patient Stack --")
patient_stack.display()

print("\n-- Undo Stack --")
undo_stack.show_info()

print("\n-- Undoing Last Action --")
undo_stack.undo_last_info()








