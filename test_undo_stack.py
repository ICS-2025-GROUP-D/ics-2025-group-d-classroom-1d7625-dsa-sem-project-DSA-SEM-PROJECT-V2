import unittest
from io import StringIO
import sys

# The class definitions should be imported or copied from your main file
# For now, we’ll assume they are already defined above or imported accordingly

class TestPatientStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(3)
        self.undo = Undo()
        self.p1 = Patient("Alice", 101, "Flu")
        self.p2 = Patient("Bob", 102, "Malaria")
        self.p3 = Patient("Carol", 103, "Covid")

    def test_push_and_display(self):
        self.stack.push(self.p1)
        self.stack.push(self.p2)
        self.assertEqual(len(self.stack.stack), 2)
        self.assertEqual(str(self.stack.stack[0]), "Alice, 101, Flu")

    def test_stack_max_capacity(self):
        self.stack.push(self.p1)
        self.stack.push(self.p2)
        self.stack.push(self.p3)
        # Attempt to exceed max
        self.stack.push(Patient("David", 104, "Headache"))
        self.assertEqual(len(self.stack.stack), 3)

    def test_update_patient(self):
        self.stack.push(self.p1)
        old_info, updated = self.stack.update_Patient(101, new_name="Alicia", new_illness="Cold")
        self.assertIsNotNone(updated)
        self.assertEqual(updated.name, "Alicia")
        self.assertEqual(updated.illness, "Cold")

    def test_delete_patient(self):
        self.stack.push(self.p1)
        self.stack.push(self.p2)
        removed = self.stack.delete_patient(101)
        self.assertEqual(str(removed), "Alice, 101, Flu")
        self.assertEqual(len(self.stack.stack), 1)

    def test_undo_push_log(self):
        self.undo.add_info("Added", self.p1)
        self.assertFalse(self.undo.undo_stack.is_empty())
        result = self.undo.undo_stack.pop()
        self.assertIn("Added Alice", result)

    def test_undo_last_info_output(self):
        self.undo.add_info("Deleted", self.p2)
        # Capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        self.undo.undo_last_info()
        sys.stdout = sys.__stdout__
        self.assertIn("Undoing: Deleted Bob", captured_output.getvalue())

    def test_pop_empty_stack(self):
        result = self.stack.pop()
        self.assertEqual(result, "The stack has nothing(empty)")

    def test_display_empty(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.stack.display()
        sys.stdout = sys.__stdout__
        self.assertIn("Stack is empty", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()
