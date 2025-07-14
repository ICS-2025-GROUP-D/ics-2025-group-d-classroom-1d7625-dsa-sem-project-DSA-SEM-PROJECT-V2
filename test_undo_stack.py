def test_stack():
    print("=== Stack Test Start ===")

    # Create a stack with max size 3
    stack = Stack(max_size=3)

    # Test is_empty on new stack
    print("Is stack empty?", stack.is_empty())  # Expected: True

    # Push 3 patients
    stack.push("Patient A")
    stack.push("Patient D")
    stack.push("Patient G")

    stack.push("Patient B")

    stack.display()

    popped = stack.pop()
    print(f"Popped item: {popped}")

    stack.display()

    stack.pop()
    stack.pop()

    print("Trying to pop from empty stack:", stack.pop())

    stack.display()
    print("Is stack empty?", stack.is_empty())

    print("=== Stack Test End ===")

test_stack()
