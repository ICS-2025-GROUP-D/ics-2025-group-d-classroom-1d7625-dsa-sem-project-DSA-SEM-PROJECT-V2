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

    def update_patient(self,id_number,new_name=None,new_illness=None):
        for patient in self.stack:
            if patient.id_number==id_number:
                old_info=str(patient)
                if new_name:
                    patient.name=new_name
                if new_illness:
                    patient.illness=new_illness
                return old_info,patient
        return None,None

    def delete_patient(self,id_number):
        for i in range(len(self.stack)):
            if self.stack[i].id_number==id_number:
                return self.stack.pop(i)
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
        print("6. View Undo Log")
        print("7. Exit")

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
            id_input = input("Enter ID of patient to delete: ").strip()
            if not id_input.isdigit():
                print(" Invalid input! Please enter a valid numeric ID.")
                return  # or continue, depending on your loop structure
            id_number = int(id_input)

            new_name = input("Enter new name (leave blank to skip): ").strip()
            new_illness = input("Enter new illness (leave blank to skip): ").strip()
            new_name = new_name if new_name else None
            new_illness = new_illness if new_illness else None
            old_info, updated_patient = patient_stack.update_patient(id_number, new_name, new_illness)
            if updated_patient:
                print(f"Updated to: {updated_patient}")
                undo_stack.add_info("Updated", updated_patient)
                print("\nUpdated Patient Stack:")
                patient_stack.display()  #show the updated stack

            else:
                print(" Patient not found.")

        elif choice == "4":
            id_number = int(input("Enter ID of patient to delete: "))
            removed = patient_stack.delete_patient(id_number)
            if removed:
                print(f"🗑Deleted: {removed}")
                undo_stack.add_info("Deleted", removed)
            else:
                print("Patient not found.")

        elif choice == "5":
            undo_stack.undo_last_info(patient_stack)


        elif choice == "6":
            undo_stack.show_info()

        elif choice == "7":
            print("Exiting the system.BYE BYE")
            break

        else:
            print(" Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()