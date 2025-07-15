## Complexity of `test_patient_stack()`

| Operation                     | Time Complexity | Space Complexity |
|------------------------------|------------------|------------------|
| Stack.push()                 | O(1)             | O(1)             |
| Undo.add_info()              | O(1)             | O(1)             |
| Stack.pop()                  | O(1)             | O(1)             |
| Stack.display()              | O(n)             | O(1)             |
| Undo.show_info()             | O(n)             | O(1)             |
| Undo.undo_last_info()       | O(1)             | O(1)             |
| **Total (test case overall)**| **O(n)**         | **O(n)**         |

> `n` = number of actions recorded or patients handled in the stack.
