[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qA5kWzgw)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19850358&assignment_repo_type=AssignmentRepo)

# DSA-SEM-PROJECT-

DATA STRUCTURES AND ALGORITHMS SEMESTER PROJECT

# USER GUIDE

## Overview

This desktop application helps you manage notes using core data structures (Stack, Queue, Linked List, Graph) with a Tkinter GUI and MongoDB for data storage. You can add, view, edit, and delete notes, and use revision features powered by custom data structures.

---

## Installation

1. **Requirements:**

   - Python 3.8+
   - `tkinter` (usually included with Python)
   - `pymongo` (install via `pip install pymongo`)
   - MongoDB running locally (default connection: `mongodb://localhost:27017`)

2. **Setup:**
   - Clone or download this repository.
   - Ensure MongoDB is running on your machine.
   - Install dependencies:
     ```sh
     pip install pymongo
     ```
   - Run the application:
     ```sh
     python main.py
     ```

---

## Quick Start

1. **Launch the app:**
   - Run `main.py` as described above.
2. **Main Window:**
   - The main window displays all notes in a table.
   - Use the buttons to read, select, and add notes to revision structures.
3. **Tabs:**
   - **Data Operations:** Add or delete notes. Select a note to edit or delete.
   - **All Notes:** Browse notes sequentially (Linked List). Use 'Next Note' and 'Restart Notes'.
   - **Revision Stack:** Add notes to a stack and review them in LIFO order.
   - **Revision Queue:** Add notes to a queue and review them in FIFO order.
   - **Frequent Paths:** View the graph of note relationships (adjacency list).

---

## Features

- **CRUD Operations:**
  - Add, view, and delete notes from the database.
- **Revision Stack:**
  - Add notes to a stack and review them in reverse order.
- **Revision Queue:**
  - Add notes to a queue and review them in order added.
- **Linked List Navigation:**
  - Browse all notes one by one, looping back to the start.
- **Graph Visualization:**
  - See how notes are connected based on your revision activity.

---

## Navigation & Usage

- **Adding a Note:**
  - Go to 'Data Operations', enter title and description, click 'Add Note'.
- **Deleting a Note:**
  - Select a note in the table, click 'Show Selected Note', then 'Delete Note'.
- **Revision Stack/Queue:**
  - Select a note, add to stack/queue, then use 'Start Revision' and 'Next Note' to review.
- **Frequent Paths:**
  - Shows a text-based graph of note relationships.

---

## Common Troubleshooting Situations

- **MongoDB Connection Error:**
  - Ensure MongoDB is running locally on port 27017.
- **Missing Dependencies:**
  - Run `pip install pymongo`.
- **GUI Issues:**
  - Make sure you are running with Python 3 and have Tkinter installed.

---

## Support

For help, contact the instructor at [bgithenya@strathmore.edu](mailto:bgithenya@strathmore.edu).

---

## Screenshots

(Add screenshots of the main window, tabs, and features here before submission.)

---

## Credits

- Developed by: (Add your names and registration numbers)
- For DSA Semester Project, Strathmore University

#
