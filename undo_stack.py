class Patient:
    def __init__(self, name, id_number, illness):
        self.name = name
        self.id_number = id_number
        self.illness = illness

    def __str__(self):
        return f"{self.name}, {self.id_number}, {self.illness}"

class Stack:
    def __init__(self,max_size):
        self.stack = []
        self.max_size=max_size

    def push(self, item):
        if len(self.stack)>=self.max_size:
            print("Stack id Full!!Cannot Add more patients")
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

    def update_patient(self, id_number, new_name=None, new_illness=None):
        if self.is_empty():
            print("Stack is empty - no update possible.")
            return None, None

        top_patient = self.stack[-1]
        if top_patient.id_number == id_number:
            old_patient = Patient(top_patient.name, top_patient.id_number, top_patient.illness)
            if new_name:
                top_patient.name = new_name
            if new_illness:
                top_patient.illness = new_illness
            return old_patient, top_patient
        else:
            print(f"Update failed: Top patient ID is {top_patient.id_number}, not {id_number}.")
            return None, None

    def delete_patient(self,id_number):
        if self.is_empty():
            print("Stack is empty-Nothing can be deleted")
            return None
        top_patient=self.stack[-1]
        if top_patient.id_number==id_number:
            return self.stack.pop()
        else:
            print(f"Top patient ID is {top_patient.id_number}, not {id_number}. Cannot delete.")
            return None

class Undo:
    def __init__(self):
        self.undo_stack = Stack(10)

    def add_info(self, action, patient):
        self.undo_stack.push((action, patient))  # store tuple

    def undo_last_info(self, patient_stack):
        if self.undo_stack.is_empty():
            print("Nothing to undo in stack")
            return
        action, patient = self.undo_stack.pop()
        print(f"Undoing: {action} {patient}")
        if action == "Deleted":
            # Re-add patient
            if len(patient_stack.stack) < patient_stack.max_size:
                patient_stack.push(patient)
                print(" Patient restored to stack.")
            else:
                print(" Cannot undo delete — patient stack is full.")
        elif action == "Added":
            patient_stack.delete_patient(patient.id_number)
            print(" Patient addition undone.")

        elif action == "Updated":
            patient_stack.update_patient(
                patient.id_number,
                new_name=patient.name,
                new_illness=patient.illness
            )
            print(" Update undone — patient info restored.")
    def show_info(self):
        self.undo_stack.display()


def main():
    MAX_STACK_SIZE = 5
    patient_stack = Stack(MAX_STACK_SIZE)
    undo_stack = Undo()

    while True:
        print("\n--- Patient Stack System ---")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Undo Last Action")
        print("6. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == "1":
            if len(patient_stack.stack) >= patient_stack.max_size:
                print("Stack full. Cannot add more patients.")
                continue
            name = input("Enter patient name: ")
            id_input = input("Enter ID number: ").strip()
            if not id_input.isdigit():
                print(" Invalid input! Please enter a numeric ID.")
                continue
            id_number = int(id_input)

            illness = input("Enter illness: ")
            new_patient = Patient(name, id_number, illness)
            patient_stack.push(new_patient)
            undo_stack.add_info("Added", new_patient)

        elif choice == "2":
            patient_stack.display()

        elif choice == "3":
            id_input = input("Enter ID of patient to update(top): ").strip()
            if not id_input.isdigit():
                print(" Invalid input! Please enter a valid numeric ID.")
                return  # or continue, depending on your loop structure
            id_number = int(id_input)

            new_name = input("Enter new name (leave blank to skip): ").strip()
            new_illness = input("Enter new illness (leave blank to skip): ").strip()
            new_name = new_name if new_name else None
            new_illness = new_illness if new_illness else None
            old_patient, updated_patient = patient_stack.update_patient(id_number, new_name, new_illness)
            if updated_patient:
                print(f"Updated to: {updated_patient}")
                undo_stack.add_info("Updated", old_patient)
                patient_stack.display()

            else:
                print(" Patient not found.Update failed!!")


        elif choice == "4":
            id_input = input("Enter ID of patient to delete(top): ").strip()
            if not id_input.isdigit():
                print(" Invalid input! Please enter a valid numeric ID.")
                continue
            id_number = int(id_input)
            removed = patient_stack.delete_patient(id_number)
            if removed:
                print(f"Deleted: {removed}")
                undo_stack.add_info("Deleted", removed)
            else:
                print("Patient not found(Only remove top patient).")

        elif choice == "5":
            undo_stack.undo_last_info(patient_stack)

        elif choice == "6":
            print("Exiting the system.BYE BYE")
            break

        else:
            print(" Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()


