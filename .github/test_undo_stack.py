from stack import Patient, Stack, Undo

def test_patient_stack():
    # Setup
    p1 = Patient("Joseph", 10045, "Malaria")
    p2 = Patient("Maria", 10047, "Typhoid")

    patient_stack = Stack()
    undo_stack = Undo()

    print(">>> Test: Adding Joseph")
    patient_stack.push(p1)
    undo_stack.add_info("Added", p1)

    print(">>> Test: Adding Maria")
    patient_stack.push(p2)
    undo_stack.add_info("Added", p2)

    print(">>> Test: Deleting last patient (Maria)")
    removed = patient_stack.pop()
    if isinstance(removed, Patient):
        undo_stack.add_info("Deleted", removed)

    print("\n>>> Final Patient Stack:")
    patient_stack.display()

    print("\n>>> Undo Stack History:")
    undo_stack.show_info()

    print("\n>>> Test: Undo Last Action")
    undo_stack.undo_last_info()

    print("\n>>> Test Complete")

# Run the test
if __name__ == "__main__":
    test_patient_stack()
