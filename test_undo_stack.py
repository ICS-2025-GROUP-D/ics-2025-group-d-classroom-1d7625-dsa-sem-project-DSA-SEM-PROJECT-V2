def test_patient_stack():
    print("=== TEST PATIENT STACK ===")

    # Create patients
    p1 = Patient("Joseph", 10045, "Malaria")
    p2 = Patient("Maria", 10047, "Typhoid")

    # Create stacks
    patient_stack = Stack()
    undo_stack = Undo()

    print("\n>>> Adding Joseph")
    patient_stack.push(p1)
    undo_stack.add_info("Added", p1)

    print("\n>>> Adding Maria")
    patient_stack.push(p2)
    undo_stack.add_info("Added", p2)

    print("\n>>> Removing Last Patient (Maria)")
    removed = patient_stack.pop()
    if isinstance(removed, Patient):
        undo_stack.add_info("Deleted", removed)

    print("\n>>> Current Patient Stack:")
    patient_stack.display()

    print("\n>>> Undo History:")
    undo_stack.show_info()

    print("\n>>> Undoing Last Action:")
    undo_stack.undo_last_info()

    print("\n>>> Final Undo History:")
    undo_stack.show_info()

    print("\n Test Complete")

# Run the test if this file is executed directly
if __name__ == "__main__":
    test_patient_stack()
