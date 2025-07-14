[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qA5kWzgw)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19850357&assignment_repo_type=AssignmentRepo)
# DSA-SEM-PROJECT-
DATA STRUCTURES AND ALGORITHMS SEMESTER PROJECT
MOVIE WATCHLIST TRACKER

A desktop application for managing your movie watchlist, implementing four core data structures with a Tkinter GUI and SQLite database.

FEATURES

- CRUD Operations: Add, view, edit, and delete movies
- Instant Search: O(1) title lookup using hash tables
- Automatic Sorting: Alphabetical sorting via BST
- Watchlist Queue: Track movies to watch (FIFO)
- Watched History: Recently viewed movies (LIFO)
- Visual Indicators: Star ratings and status colors

DATA STRUCTURES USED

1. Hash Table
   - Purpose: Instant movie lookup by title
   - Key Operations: Search/Insert/Delete
   - Complexity: O(1) average case

2. Binary Search Tree (BST)
   - Purpose: Alphabetical sorting of movies
   - Key Operations: In-order traversal
   - Complexity: O(log n) average case

3. Queue
   - Purpose: Watchlist (first-in-first-out)
   - Key Operations: Enqueue/Dequeue
   - Complexity: O(1)

4. Stack
   - Purpose: Recently watched (last-in-first-out)
   - Key Operations: Push/Pop
   - Complexity: O(1)

INSTALLATION

1. Prerequisites:
   - Python 3.8+
   - Tkinter (usually included with Python)

2. Run the application:
   git clone https://github.com/yourusername/movie-watchlist-tracker.git
   cd movie-watchlist-tracker
   python gui.py

USAGE

MAIN INTERFACE

1. Add Movie:
   - Click "Add Movie" button
   - Fill in title, genre, rating (1-5), and year
   - Movie appears in watchlist

2. Search:
   - Type in search box for instant filtering

3. Mark Watched:
   - Select movie and click "Mark Watched"
   - Moves from Watchlist to Recently Watched

4. Edit/Delete:
   - Select movie and use corresponding buttons

DATABASE SCHEMA

The SQLite database (movie_watchlist.db) contains one table:

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL,
    genre TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    year INTEGER,
    watched BOOLEAN DEFAULT 0
)

MADE BY:
FUAD ISSA
GRACE MESSO
LENNY GITHUI
DIANA KITONYI
DARLENE NYABOKE
DANIELA JONES
