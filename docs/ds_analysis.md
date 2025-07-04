# Binary Search Tree (BST) - Analysis

## Use in Hospital System
Used to store patients in order based on their ID.
Helps search, insert, and delete efficiently in sorted order.

## Methods
- insert(id, name, age, illness)
- search(id)
- delete(id)
- inorder()

## Time & Space Complexity

| Operation | Avg Time | Worst Time | Space |
|-----------|----------|------------|-------|
| Insert    | O(log n) | O(n)       | O(n)  |
| Search    | O(log n) | O(n)       | O(1)  |
| Delete    | O(log n) | O(n)       | O(1)  |
